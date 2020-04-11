# views.py

from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, PalindromeForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        print(form.username.data)
        return redirect('/')
    return render_template('index.html', title='Sign In', form=form)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/challenges', methods=['GET', 'POST'])
def palindrome():
    form = PalindromeForm()
    if form.validate_on_submit():
        flash('String requested {}'.format(form.string.data))
        print(form.string.data)
        # Program to check if a string is palindrome or not
        """
        A palindrome is a word, phrase, number or sequence of words 
        that reads the same backward as forward
        """

        my_str = form.string.data

        # make it suitable for caseless comparison
        my_str = my_str.casefold()

        # reverse the string
        rev_str = reversed(my_str)

        # check if the string is equal to its reverse
        if list(my_str) == list(rev_str):
            print("The string is a palindrome.")
            flash("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
            flash("The string is not a palindrome.")
        return redirect('/challenges')
    return render_template("challenges.html", title='Challenges', form=form)
