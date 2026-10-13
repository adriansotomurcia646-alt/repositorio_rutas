from django.test import TestCase
from django.urls import reverse

from .models import Comment, Post


class InicioViewTests(TestCase):
    def test_muestra_publicaciones_y_comentarios_del_modelo(self):
        post = Post.objects.create(
            author="Usuario de prueba",
            content="Contenido de prueba",
        )
        Comment.objects.create(
            post=post,
            author="Comentarista",
            content="Comentario de prueba",
        )

        response = self.client.get(reverse("blog:inicio"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Usuario de prueba")
        self.assertContains(response, "Contenido de prueba")
        self.assertContains(response, "Comentarista: Comentario de prueba")

    def test_muestra_mensaje_si_no_hay_publicaciones(self):
        Post.objects.all().delete()

        response = self.client.get(reverse("blog:inicio"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aún no hay publicaciones.")
