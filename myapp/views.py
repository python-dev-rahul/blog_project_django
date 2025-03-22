from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from myapp.forms import *
from django.http import HttpResponseRedirect


def home(request):
    search_query = request.GET.get("search")
    category_show = Category.objects.all()
    try:
        if search_query:
            # Split the search query into individual words
            keywords = search_query.split()

            # Create a Q object with OR conditions for each keyword and each field
            query_condition = Q()
            for keyword in keywords:
                query_condition |= Q(title__icontains=keyword) | Q(
                    heading__icontains=keyword
                )

            # Filter posts based on the constructed query condition
            blogs = Post.objects.filter(query_condition).distinct()
            return render(request, "filtered_blogs.html", {"blogs": blogs})
        else:
            # Get only two posts for each category
            categories = Post.objects.values_list("category", flat=True).distinct()
            blogs = []
            for category in categories:
                category_posts = Post.objects.filter(category=category)[:2]
                blogs.extend(category_posts)

            context = {"blogs": blogs, "category": category_show}
            return render(request, "home.html", context)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def send_email(request):
    if request.method == "POST":
        user_email = request.POST.get("user_email")
        if user_email == "":
            return JsonResponse({"error": "Please enter your email"}, status=400)

        # Send confirmation email to user
        user_subject = "Thank You for Contacting Us"
        user_message = render_to_string(
            "user_email_template.txt", {"user_email": user_email}
        )
        user_email_message = EmailMessage(user_subject, user_message, to=[user_email])
        user_email_message.send()

        # Send email to admin
        subject = "New Contact Form Submission"
        message = f"User Email: {user_email}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.EMAIL_HOST_USER]  # Replace with your admin email address
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return render(request, "choosing_us.html")  # Redirect to a thank you page

    return render(request, "home.html")


def show_blog_detail(request, slug):
    # print(f"Slug: {slug}")
    blog = get_object_or_404(Post, slug=slug)
    related_posts = Post.objects.filter(category=blog.category).exclude(slug=slug)

    context = {"blog": blog, "related_posts": related_posts}
    # print(blog)
    return render(request, "detail.html", context)


def all_category(request, name):
    category = get_object_or_404(Category, name=name)
    post = Post.objects.filter(category=category)
    print(post)
    return render(request, "category_post.html", {"post": post})


def admin_url(request):
    return render(request, "admin.html")


def admin_add_blog(request):
    if request.method == "POST":
        form = MyPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/admin-panel")
        else:
            pass
            # print(form.errors)  # Print form errors to the console for debugging
    else:
        form = MyPostForm()

    return render(request, "admin-add-blog.html", {"form": form})


from django.shortcuts import render
from .models import Post


def edit_blog(request):
    matching_posts = []  # Initialize an empty list

    if request.method == "POST":
        selected_category = request.POST.get("user_input_value")
        # print(selected_category)

        # Assuming you have a 'category' field in your Post model
        matching_posts = Post.objects.filter(category__name=selected_category)

        # Now 'matching_posts' contains all posts with the selected category
        for post in matching_posts:
            pass
            # print(post.title)  # Access other fields as needed

    return render(request, "edit-blog.html", {"matching_posts": matching_posts})


def updatepost(request, id):
    if request.method == "POST":
        pi = Post.objects.get(pk=id)
        form = MyPostForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/admin-panel-dreamers-infotech-abcdefgh12345684ghvyasvgvastcvbh!_+$%^&*(gFDSA)rctvybunim/")
    else:
        pi = Post.objects.get(pk=id)
        form = MyPostForm(instance=pi)
        return render(request, "admin-add-blog.html", {"form": form})


def delete_post(request, id):
    if request.method == "GET":
        pi = Post.objects.get(pk=id)
        # print(pi, "--------------------")
        pi.delete()
        return HttpResponseRedirect("/edit-blog")


def about_us(request):
    if request.method == "POST":
        user_email = request.POST.get("user_email")
        if user_email == "":
            return JsonResponse({"error": "Please enter your email"}, status=400)

        # Send confirmation email to user
        user_subject = "Thank You for Contacting Us"
        user_message = render_to_string(
            "user_email_template.txt", {"user_email": user_email}
        )
        user_email_message = EmailMessage(user_subject, user_message, to=[user_email])
        user_email_message.send()

        # Send email to admin
        subject = "New Contact Form Submission"
        message = f"User Email: {user_email}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.EMAIL_HOST_USER]  # Replace with your admin email address
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return render(request, "choosing_us.html")  # Redirect to a thank you page
    return render(request, "about_us.html")

def newsletter(request):
    return render(request,"newsletter.html")