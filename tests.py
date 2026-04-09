import pytest
from main import BooksCollector

class TestBooksCollector:

    #1. Тесты на метод __init__

    # Проверка что books_genre по умолчанию пустой
    def test_init_default_value_books_genre(self, collector):
        assert collector.books_genre == {}
    
    # Проверка что favorites по умолчанию пустой
    def test_init_default_vaslue_favorites(self, collector):
        assert collector.favorites == []
    # Проверка списка genre
    def test_init_default_value_genre(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    # Проверка списка enre_age_rating
    def test_init_default_value_genre_age_rating(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']
 
    #2. Тесты на метод add_new_book

    # Добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Добавление одной и той же книги два раза
    def test_add_new_book_double_same(self, collector):
        title = 'Что делать, если ваш кот хочет вас убить'
        assert len(collector.get_books_genre()) != 2
    
    # Добавление книги с длинным названием
    def test_add_new_book_long_name(self, collector):
        long_name = 'Test' * 15
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()
    
    #3. Тесты на метод set_book_genre

    @pytest.mark.parametrize('genre',['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])

    # Устанавливаем книге жанр
    def test_set_book_genre_valid_book_and_genre(self, collector, genre):
        title = 'Гордость и предубеждение и зомби'
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.get_book_genre(title) == genre

    # Заменяем жанр
    def test_set_book_genre_change_genre(self, collector):
        title = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(title)
        collector.set_book_genre(title, 'Ужасы')
        collector.set_book_genre(title, 'Фантастика')
        assert collector.get_book_genre(title) == 'Фантастика'
    
    # Устанавливаем жанр которого нет в списке genre
    def test_set_book_genre_invalid_genre(self, collector):
        title = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(title)
        collector.set_book_genre(title, 'Аниме')
        assert collector.get_book_genre(title) != 'Аниме'

    #4. Тесты на метод get_book_genre

    def test_get_book_genre_valid_book(self, collector):
        title = 'Гордость и предубеждение и зомби'
        collector.add_new_book(title)
        collector.set_book_genre(title, 'Комедии')
        assert collector.get_book_genre(title) == 'Комедии'

    def test_get_book_genre_book_with_empty_genre(self, collector):
        title = 'Гордость и предубеждение и зомби'
        collector.add_new_book(title)
        assert collector.get_book_genre(title) == ''

    #5. Тест на метод get_books_with_specific_genre

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        titles_genres = {
        '1984': 'Фантастика',
        'Граф Монте-Кристо': 'Детективы',
        'Три мушкетера': 'Комедии',
        'Дракула': 'Ужасы',
        'Алиса в Стране чудес': 'Мультфильмы',
        'О дивный новый мир': 'Фантастика'
        }
        for k, v in titles_genres.items():
            collector.add_new_book(k)
            collector.set_book_genre(k, v)
        assert collector.get_books_with_specific_genre('Фантастика') == ['1984', 'О дивный новый мир']

    # 6. Тест на метод get_books_genre

    @pytest.mark.parametrize(
        'title',
        [
            ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби'],
            ['Что делать, если ваш кот хочет вас убить'],
            []
        ]
    )

    # Добавляем и проверяем, что названия книг в books_genre соответствуют title

    def test_get_books_genre(self, collector, title):

        # добавляем книги в books_genre
        for i in title:
            collector.add_new_book(i)
        assert list(collector.get_books_genre().keys()) == title
    
    # 7. Проверка метода get_books_for_children

    def test_get_books_for_children_age_rating(self, collector):
        title_1 = 'Хоббит'
        title_2 = 'Сияние'
        collector.add_new_book(title_1)
        collector.add_new_book(title_2)
        collector.set_book_genre(title_1, 'Фантастика')
        collector.set_book_genre(title_2, 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert  books_for_children == [title_1]

    # 8. Проверка метода add_book_in_favorites

    def test_add_book_in_favorites(self, collector):
        title = 'На западном фронте без перемен'
        collector.add_new_book(title)
        collector.add_book_in_favorites(title)
        assert title in collector.get_list_of_favorites_books()
    
    # 9. Проверка метода delete_book_from_favorites

    def test_delete_book_from_favorites(self, collector):
        title = 'Война и Мир'
        collector.add_new_book(title)
        collector.add_book_in_favorites(title)
        collector.delete_book_from_favorites(title)
        assert 'Война и Мир' not in collector.get_list_of_favorites_books()

    #10. Проверка метода get_list_of_favorites_books

    def test_get_list_of_favorites_books(self, collector):
        title_1 = 'Искра жизни'
        title_2 = 'Мастер и Маргарита'
        collector.add_new_book(title_1)
        collector.add_new_book(title_2)
        collector.add_book_in_favorites(title_1)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == [title_1]

