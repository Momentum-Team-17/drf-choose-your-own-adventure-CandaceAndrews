# Choose Your Own API Adventure

Choose one of the following options. In both cases you are building an application that serves JSON, not HTML. You are not concerning yourself with the display of the information, only the functionality.

**The application you build must be deployed, whichever option you choose. 🚀**

## Option 1: Habit Tracker API

Continue working in your existing Habit Tracker repo -- that is, not this repo! Add a new app to your project and call it `api` (`python manage.py startapp api`). Your app should provide CRUD endpoints that return JSON responses, but provide the _same functionality_ as your original habit tracker.

This API should be _in addition to_, not _in replacement of_, the existing habit tracker application you have already built. You do not need to touch the templates or views you wrote for that app.

Your API should provide endpoints to do all of the following:

- list habits for the logged in user
- create a new habit associated with the logged in user
- update a habit if you are the creator of the habit
- delete a habit if you are the creator of the habit
- get data about a specific habit that includes its associated daily records, if any, if you are the owner of the habit
- create a record for a habit for today (stretch: create a record for any date), if you are the owner of the habit
- update a record for a habit if you are the creator of the habit
- delete a record from a habit if you are the creator of the habit

Write up a list of endpoints you think you will need before you start doing this. Don't make endpoints you don't need. NOTE: there is not a one-to-one correspondence between the endpoints you make and pages on a front end application that might use your API. 

You should develop and test your endpoints using Insomnia. You can also use the browsable API that DRF gives you in the browser, but you should be comfortable using Insomnia.

## Option 2: DRF Library API

Create a new API-only application that lets users keep track of books, including important information like title, author, publication date, a genre, and a field that marks it as "featured". Books should be unique by title and author (that is, you can't have two books with the same title _and_ author; two books with the same title is fine as long as the authors are different).

Users should be able to search for a book by title or author.

Anyone can add a new book as long as the same book is not already in the library. Only admin users can update book details (like whether it is "featured") and delete books.

You'll also need a book tracking model so that users can mark a book as "want to read", "reading", or "read/done"; this status can also be updated. The tracking model should have a foreign key to a book and to a user.

Optionally users can take notes on books. These notes have a foreign key relationship with a book and a user, a datetime they are created, a note body, a boolean field marking it as public or private, and an optional page number. Private notes are viewable only by the author. When notes are retrieved, return them by creation time in reverse order.

Users should be able to see a list of all the books they are tracking, or a list by status (for instance, all their "want to read" books). You _could_ consider using [DjangoFilterBackend](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend) for this.

You should _not_ make forms or templates for this app, but you will need models, urls, views, and serializers. You should use class-based views and return JSON responses.

Your app should allow users to:

- list all books
- list all featured books
- create a book
- retrieve details about a book
- search books by author or title
- see a list of all the books they are tracking and their statuses
- mark a book as want to read, reading, or read
- update the want to read/reading/read status of a book
- see a list of all their books by status (e.g., all the books they have marked as "read")
- retrieve all their own private notes for a book
- retrieve all public notes for a book
- create a note for a book
- edit their own notes

Admin users can:

- update a book (including marking/unmarking it as featured)
- delete a book (this should not delete notes about a book)

You'll need to use Insomnia (or some other tool for making requests) to test your API as you are building it.
