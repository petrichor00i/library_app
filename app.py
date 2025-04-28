import os
from flask import Flask, render_template, request, redirect
from database import add_book, get_all_books, get_book_by_id, update_book, delete_book, search_books
import analysis
from flask import flash

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', '12345678')


@app.route('/')
def index():
    books = get_all_books()
    return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book_route():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        add_book(title, author, year, genre)
        return redirect('/')
    return render_template('add_book.html')


@app.route('/report')
def report():
    report_data = analysis.get_genre_report()
    return render_template('report.html', report=report_data)


@app.route('/search', methods=['GET', 'POST'])
def search():
    books = []
    if request.method == 'POST':
        keyword = request.form['keyword']
        books = search_books(keyword)
    return render_template('search.html', books=books)


@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        update_book(book_id, title, author, year, genre)
        flash('Book updated Successfully!')
        return redirect('/')

    book = get_book_by_id(book_id)
    return render_template('edit_book.html', book=book)


@app.route('/delete/<int:book_id>')
def delete(book_id):
    delete_book(book_id)
    flash('Book Deleted Successfully!')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
