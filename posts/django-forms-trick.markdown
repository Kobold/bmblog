Type: post
Title: Django Forms-fu
Date: July 15, 2009

Today I ran into an issue where I wanted to change the options for a
form field based upon what was selected in other fields. Employers use
this particular form to create a job opening. First, they select the
type of job they're creating (e.g. Waitstaff, Flight Attendant,
Programmer, etc.) and then they choose from a list of hiring policies
that depends on the type of job.

By default Django's `ModelForm` sees the hiring policy foreign key for
the job opening and lets you select from all of hiring policies for
any type of job. I found out how to [filter form querysets from
StackOverflow][1]. The next issue was how to actually do the updating
once a user chose a job type.

I ended up adding some Javascript to POST when the job type selection
changed. This worked exactly as needed. The only issue is that because
the form is (usually) incompletely filled out, the page was covered in
"field required" errors. Someone in the #django IRC channel suggested
hiding the errors on the page, but I couldn't find any good way of
suppressing these.

So, `Form(request.POST)` leads to errors all over the page.

My next try was with the form's `initial` argument. This is one way to
give the form data without actually processing it. The thing is,
`Form(initial=request.POST)` doesn't do what you think it does. If you
do that, all your form fields will end up filled with Python list
literals. `request.POST` is a [`QueryDict`][2] and not a normal
`dict`. Its contents look something like:

    {u'salary': [u''], u'city': [u''], u'zip': [u''], ... }

Because queries can post multiple values for the same key, the values
in the `QueryDict` are lists of values. I just want a normal `dict` to
pass to `initial` though. The solution?

`Form(initial=dict(request.POST.items()))`

Why?

    >>> request.POST
    <QueryDict: {u'salary': [u'500', u'600'], u'city': [u''], ... u'salary_type': [u'']}>
    >>> dict(request.POST.items())
    {u'salary': u'600', u'city': u'', ... u'salary_type': u''}

[1]:
http://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform
[2]: http://docs.djangoproject.com/en/dev/ref/request-response/#querydict-objects
