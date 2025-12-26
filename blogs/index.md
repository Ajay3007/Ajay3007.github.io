---
layout: default
title: Blogs
---

# Blogs

Welcome to the blogs index. Below are posts in the `blogs` category.

<ul>
{% for post in site.posts %}
	{% if post.categories contains 'blogs' %}
	<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> — <time>{{ post.date | date: "%B %d, %Y" }}</time></li>
	{% endif %}
{% endfor %}
</ul>

[Back to home]({{ '/' | relative_url }})
