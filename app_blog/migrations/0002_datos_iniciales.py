from django.db import migrations


POSTS = [
    (
        "Usuario 1",
        "GTA VI se retrasa otros 3 meses",
        [
            ("Usuario 1", "Que mal, ya lo estaba esperando"),
            ("usuario 2", "ya mejor no hagan nada"),
            ("usuario3", "y sin formato fisico"),
        ],
    ),
    (
        "Usuario 2",
        "Nuevo decreto por parte del presidente de la republica",
        [
            ("Usuario 1", "Ya la verdad no importa lo que diga"),
            ("usuario 2", "El poder pierde credebilidad"),
            ("usuario3", "No es lo que habia prometido"),
        ],
    ),
    (
        "Usuario 3",
        "Mi torre se apaga o reinicia cada rato",
        [
            ("Usuario 1", "Puede ser la fuente de poder"),
            ("usuario 2", "Tal vez se te daño la fuente por falta de una ups"),
            ("usuario3", "Llevala a un tecnico"),
        ],
    ),
]


def crear_datos_iniciales(apps, schema_editor):
    Post = apps.get_model("app_blog", "Post")
    Comment = apps.get_model("app_blog", "Comment")

    for author, content, comments in POSTS:
        post = Post.objects.create(author=author, content=content)
        Comment.objects.bulk_create(
            [
                Comment(post=post, author=comment_author, content=comment_content)
                for comment_author, comment_content in comments
            ]
        )


def eliminar_datos_iniciales(apps, schema_editor):
    Post = apps.get_model("app_blog", "Post")
    Comment = apps.get_model("app_blog", "Comment")

    for author, content, _ in POSTS:
        post_ids = Post.objects.filter(author=author, content=content).values_list(
            "id",
            flat=True,
        )
        Comment.objects.filter(post_id__in=post_ids).delete()
        Post.objects.filter(author=author, content=content).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("app_blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(crear_datos_iniciales, eliminar_datos_iniciales),
    ]
