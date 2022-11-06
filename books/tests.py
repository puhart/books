from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse
from .models import Book


class BookTests(TestCase):

    def setUp(self):
        # self.user = get_user_model.objects.create_user(
        #     username = 'reviewuser',
        #     email = 'reviewuser@email.com',
        #     password = 'testpass123'
        # )
        # self.permission = Permission.objects.get(
        #     codename='special_status'
        # )
        self.book = Book.objects.create(
            title = 'Harry Potter',
            author = 'JK Rowling',
            price = '25.00',
        )

        # self.review = Review.objects.create(
        #     book = self.book,
        #     author = self.user,
        #     review = 'An excellent book!'
        # )

    # def test_book_list_for_logged_in_user(self):
    #     self.client.login(email='reviewuser@email', password='testpass123')
    #     response = self.client.get(reverse('book_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Harry Potter')
    #     self.asserTemplateUsed(response, 'books/book_list.html')

    # def test_book_list_for_logged_in_user(self):
    #     self.client.logout())
    #     response = self.client.get(reverse('book_list'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(
    #         response, '%s?next=/books/' % (reverse('account_login')))
    #     response = self.client.get(
    #         '%s?next=/books/' % (reverse('account_login')))
    #     self.assertContains(response, 'Log In')

    # def test_book_detail_view_with_permissions(self):
        
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertNotContains(response, 'An excellent book!')
        self.assertTemplateUsed(response, 'books/book_detail.html')