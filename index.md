---
layout: default
title: Home
---

# 👋 Welcome to Calculusphile

My personal hub for projects, blogs, and learning resources in programming and Computer Science & Engineering.


<div style="text-align:center; margin:1rem 0;">
    <a href="https://youtube.com/@calculusphile?si=ZXuiXQ2fsTA3Fhax" target="_blank" rel="noopener noreferrer" style="display:inline-block; background:#FF0000; color:white; padding:0.5rem 1rem; border-radius:6px; text-decoration:none; font-weight:600;">▶️ Subscribe on YouTube</a>
</div>

<div class="home-top">
    <div class="hf-tabs">
        <div class="hf-tab active" data-target="overview">Overview</div>
        <div class="hf-tab" data-target="activity">Activity</div>
    </div>

    <div class="home-search">
        <input id="home-search" type="search" placeholder="Search projects & posts..." aria-label="Search" />
        <a href="{{ '/projects' | relative_url }}" role="button">All Projects</a>
    </div>

    <div id="overview" class="hf-panel active">
        <div class="blog-hero">
            <h2>Quick Overview</h2>
            <p>Recent projects, blog posts, and learning highlights — interactive and filterable.</p>
        </div>
    </div>

    <div id="activity" class="hf-panel">
        <div class="activity-list">
            <div class="col">
                <h3>Recent Projects</h3>
                <div class="projects-list">
                    {% for project in site.projects limit:3 %}
                    <div class="project-card">
                        <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
                        {% if project.description %}<p>{{ project.description }}</p>{% endif %}
                    </div>
                    {% endfor %}
                </div>
            </div>
            <div class="col">
                <h3>Recent Posts</h3>
                <ul>
                    {% for post in site.posts limit:5 %}
                    <li class="home-post-item">**[{{ post.title }}]({{ post.url }})** - <time>{{ post.date | date: "%b %d, %Y" }}</time></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
</div>

## 🚀 Latest Projects

<div class="projects-list">
    {% for project in site.projects limit: 3 %}
    <div class="project-card">
        <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
        {% if project.description %}
            <p>{{ project.description }}</p>
        {% endif %}
    </div>
    {% endfor %}
</div>


[View All Projects →]({{ '/projects' | relative_url }})


## 📝 Latest Blog Posts

{% for post in site.posts limit: 3 %}
- **[{{ post.title }}]({{ post.url }})** - <time>{{ post.date | date: "%B %d, %Y" }}</time>
{% endfor %}

[Read More Posts →]({{ '/blogs' | relative_url }})


## 📚 Learning Journey

Explore topic-wise paths and quick intros below.

<div class="projects-list">
    <div class="project-card">
        <h3><a href="{{ '/learning/dsa/' | relative_url }}">Data Structures & Algorithms</a></h3>
        <p>Fundamentals, implementations, and problem-solving patterns.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/system-design/' | relative_url }}">System Design</a></h3>
        <p>High-level architecture, scalability, and trade-offs.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/oop/' | relative_url }}">OOPs</a></h3>
        <p>Core principles, SOLID, and design patterns.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/operating-systems/' | relative_url }}">Operating Systems</a></h3>
        <p>Processes, memory, scheduling, and concurrency.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/networking/' | relative_url }}">Networking</a></h3>
        <p>Protocols, routing, TCP/UDP and practical networking.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/competitive-programming/' | relative_url }}">Competitive Programming</a></h3>
        <p>Contest strategy, patterns and practice resources.</p>
    </div>
    <div class="project-card">
                <h3><a href="{{ '/learning/ai-ml/' | relative_url }}">AI & ML</a></h3>
                <p>Introductory ML concepts, models and projects.</p>
    </div>
</div>

[Explore full learning index →]({{ '/learning' | relative_url }})


## CSE BTech Curriculum

Explore program-specific curriculum:

<div class="projects-list">
    <div class="project-card">
        <h3><a href="{{ '/learning/CSE%20BTech/' | relative_url }}">CSE B.Tech (IIIT Pune)</a></h3>
        <p>Semester-wise course structure and subject intros.</p>
    </div>
</div>


## 💡 About This Site

This portfolio showcases my journey in programming, learning data structures & Algorithm during my Computer Science Engineering. Feel free to explore my work and [learn more about me]({{ '/about' | relative_url }}).

