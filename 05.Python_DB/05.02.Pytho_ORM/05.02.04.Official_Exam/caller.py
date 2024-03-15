import os
import django
from django.db.models import Q, Count, Avg, Sum

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review


# Create and run your queries within functions
def get_authors(search_name=None, search_email=None):
    authors = None

    if not search_name and not search_email:
        return ""

    elif search_name and search_email:
        authors = Author.objects.filter(
            Q(full_name__icontains=search_name) &
            Q(email__icontains=search_email)
        ).order_by(
            '-full_name',
        )

    elif search_name and not search_email:
        authors = Author.objects.filter(
            Q(full_name__icontains=search_name)
        ).order_by(
            '-full_name',
        )

    elif not search_name and search_email:
        authors = Author.objects.filter(
            Q(email__icontains=search_email)
        ).order_by(
            '-full_name',
        )

    if not authors:
        return ""

    result = []

    for author in authors:
        result.append(
            f"Author: {author.full_name}, "
            f"email: {author.email}, "
            f"status: {'Banned' if author.is_banned else 'Not Banned'}"
        )

    return '\n'.join(result)


def get_top_publisher():
    top_publisher = Author.objects.annotate(
            total_articles=Count('article'),
        ).order_by(
            '-total_articles',
            'email',
        ).first()

    if not top_publisher or top_publisher.total_articles == 0:
        return ""

    return f"Top Author: {top_publisher.full_name} with {top_publisher.total_articles} published articles."


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(
        total_reviews=Count('review'),
    ).order_by(
            '-total_reviews',
            'email',
        ).first()

    if not top_reviewer or top_reviewer.total_reviews == 0:
        return ""

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.total_reviews} published reviews."


def get_latest_article():
    last_article = Article.objects.annotate(
        sum_rating=Sum('review__rating'),
        total_reviews=Count('review'),
    ).order_by(
        '-published_on',
    ).first()

    if last_article is None or last_article.authors.all == 0:
        return ""

    last_article_authors = last_article.authors.all().order_by(
        'full_name'
    )

    last_article_authors_names = ', '.join(
        [author.full_name for author in last_article_authors]
    )

    last_article_num_reviews = Review.objects.filter(
        article=last_article,
    ).count()

    last_article_avg_rating = 0

    if last_article.total_reviews > 0:
        last_article_avg_rating = last_article.sum_rating / last_article.total_reviews

    return (f"The latest article is: {last_article.title}. "
            f"Authors: {last_article_authors_names}. "
            f"Reviewed: {last_article_num_reviews} times. "
            f"Average Rating: {last_article_avg_rating:.2f}.")


def get_top_rated_article():
    top_article = Article.objects.annotate(
        avg_rating=Avg('review__rating')
    ).order_by(
        '-avg_rating',
        'title',
    ).first()

    if not top_article or not top_article.avg_rating:
        return ""

    top_article_reviews = top_article.review_set.count()

    return (f"The top-rated article is: {top_article.title}, "
            f"with an average rating of {top_article.avg_rating:.2f}, "
            f"reviewed {top_article_reviews} times.")


def ban_author(email=None):
    if not email:
        return "No authors banned."

    searched_author = Author.objects.filter(
        email__exact=email,
    ).first()

    if not searched_author:
        return "No authors banned."

    author_reviews_count = searched_author.review_set.count()

    searched_author.review_set.all().delete()
    searched_author.is_banned = True

    searched_author.save()

    return (f"Author: {searched_author.full_name} is banned! "
            f"{author_reviews_count} reviews deleted.")
