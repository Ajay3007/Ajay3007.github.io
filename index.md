---
layout: default
title: Home
---

# 👋 Welcome to ajdevhub

My personal hub for projects, blogs, and learning resources in programming and Computer Science & Engineering.


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
        <div style="display: grid; gap: 2rem;">
            <!-- Intro Section -->
            <div style="background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(255,107,157,0.08)); border-radius: 12px; padding: 2rem; border: 1px solid rgba(0,212,255,0.1);">
                <h2 style="margin: 0 0 0.75rem 0; color: var(--primary-color);">👨‍💻 Welcome</h2>
                <p style="margin: 0; color: var(--light-text); line-height: 1.8; font-size: 1.05rem;">
                    Software Engineer with 4+ years building high-performance systems in <strong>networking</strong>, <strong>data plane</strong>, and <strong>backend infrastructure</strong>. 
                    Passionate about system design, deep packet inspection, and real-time threat detection.
                </p>
            </div>

            <!-- Stats Section -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1.5rem;">
                <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: var(--shadow-sm); border-top: 3px solid var(--secondary-color); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.12)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='var(--shadow-sm)';">
                    <div style="font-size: 2.2rem; font-weight: 700; color: var(--secondary-color);">{{ site.posts | size }}</div>
                    <div style="color: var(--light-text); font-size: 0.95rem; font-weight: 600;">Blog Posts</div>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: var(--shadow-sm); border-top: 3px solid var(--accent-color); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.12)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='var(--shadow-sm)';">
                    <div style="font-size: 2.2rem; font-weight: 700; color: var(--accent-color);">{{ site.projects | size }}</div>
                    <div style="color: var(--light-text); font-size: 0.95rem; font-weight: 600;">Projects</div>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: var(--shadow-sm); border-top: 3px solid #10b981; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.12)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='var(--shadow-sm)';">
                    <div style="font-size: 2.2rem; font-weight: 700; color: #10b981;">77</div>
                    <div style="color: var(--light-text); font-size: 0.95rem; font-weight: 600;">DSA Problems</div>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 10px; text-align: center; box-shadow: var(--shadow-sm); border-top: 3px solid #9945ff; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.12)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='var(--shadow-sm)';">
                    <div style="font-size: 2.2rem; font-weight: 700; color: #9945ff;">10+</div>
                    <div style="color: var(--light-text); font-size: 0.95rem; font-weight: 600;">Topics</div>
                </div>
            </div>

            <!-- Featured: Problems Hub -->
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; padding: 2rem; position: relative; overflow: hidden; box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);">
                <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: rgba(255,255,255,0.1); border-radius: 50%;"></div>
                <div style="position: absolute; bottom: -30px; left: -30px; width: 150px; height: 150px; background: rgba(255,255,255,0.1); border-radius: 50%;"></div>
                <div style="position: relative; z-index: 1;">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <span style="font-size: 3rem;">🎯</span>
                        <div>
                            <h2 style="margin: 0; color: white; font-size: 1.8rem;">Practice Problems Hub</h2>
                            <p style="margin: 0.25rem 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.05rem;">Master DSA with 77 curated problems across 6 topics</p>
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
                        <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 8px; text-align: center; backdrop-filter: blur(10px);">
                            <div style="font-size: 1.8rem; font-weight: bold; color: white;">43</div>
                            <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Problems Solved</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 8px; text-align: center; backdrop-filter: blur(10px);">
                            <div style="font-size: 1.8rem; font-weight: bold; color: #4ade80;">78%</div>
                            <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Success Rate</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 8px; text-align: center; backdrop-filter: blur(10px);">
                            <div style="font-size: 1.8rem; font-weight: bold; color: white;">6</div>
                            <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Active Topics</div>
                        </div>
                    </div>
                    <a href="{{ '/problems/' | relative_url }}" style="display: inline-block; padding: 14px 32px; background: white; color: #667eea; border-radius: 10px; text-decoration: none; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: all 0.3s;" onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 6px 20px rgba(0,0,0,0.3)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 4px 15px rgba(0,0,0,0.2)';">
                        🚀 Explore All Problems
                    </a>
                </div>
            </div>

            <!-- Key Areas -->
            <div>
                <h3 style="color: var(--primary-color); margin-top: 0; margin-bottom: 1.25rem;">🎯 Quick Navigation</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
                    <a href="{{ '/problems/' | relative_url }}" style="padding: 1.25rem; background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1)); border-radius: 8px; text-decoration: none; color: var(--primary-color); border: 2px solid #667eea; transition: all 0.3s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 20px rgba(102,126,234,0.3)'; this.style.borderColor='#764ba2';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)'; this.style.borderColor='#667eea';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">🎯 Practice Problems</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">77 problems • 43 solved</div>
                    </a>
                    <a href="{{ '/learning/dsa/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #00d4ff; transition: all 0.3s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">📊 DSA & Algorithms</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Structures, patterns & theory</div>
                    </a>
                    <a href="{{ '/learning/system-design/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #ff6b9d; transition: all 0.3s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">🏗️ System Design</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Architecture & scalability</div>
                    </a>
                    <a href="{{ '/learning/networking/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #9945ff; transition: all 0.3s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">🌐 Networking</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Protocols & data plane</div>
                    </a>
                    <a href="{{ '/learning/data-plane/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #10b981; transition: all 0.3s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">⚡ Data Plane (DPDK/VPP)</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Performance optimization</div>
                    </a>
                    <a href="{{ '/learning/oop/' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #f59e0b; transition: all 0.3s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">🎯 OOP & Patterns</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Design principles</div>
                    </a>
                    <a href="{{ '/projects' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #ef4444; transition: all 0.3s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">🚀 Projects</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Real-world applications</div>
                    </a>
                    <a href="{{ '/blogs' | relative_url }}" style="padding: 1.25rem; background: white; border-radius: 8px; text-decoration: none; color: var(--primary-color); border-left: 4px solid #8b5cf6; transition: all 0.3s; box-shadow: var(--shadow-sm);" onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='none'; this.style.boxShadow='var(--shadow-sm)';">
                        <div style="font-weight: 700; margin-bottom: 0.3rem;">✍️ Blog Posts</div>
                        <div style="font-size: 0.9rem; color: var(--light-text);">Technical articles</div>
                    </a>
                </div>
            </div>
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
                    <li class="home-post-item"><a href="{{ post.url }}">{{ post.title }}</a> - <time>{{ post.date | date: "%b %d, %Y" }}</time></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
{% for post in site.posts limit: 3 %}
    <div style="background: white; border-radius: 10px; padding: 1.5rem; box-shadow: 0 2px 10px rgba(0,0,0,0.08); border-left: 4px solid #667eea; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 10px rgba(0,0,0,0.08)';">
        <time style="color: #9ca3af; font-size: 0.85rem; display: block; margin-bottom: 0.5rem;">{{ post.date | date: "%B %d, %Y" }}</time>
        <h3 style="margin: 0 0 0.75rem 0; font-size: 1.2rem;"><a href="{{ post.url }}" style="text-decoration: none; color: #2d3748;">{{ post.title }}</a></h3>
        {% if post.excerpt %}
        <p style="margin: 0; color: #64748b; font-size: 0.95rem; line-height: 1.6;">{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
        {% endif %}
    </div>
{% endfor %}
</div>

<div style="text-align: center;">
    <a href="{{ '/blogs' | relative_url }}" style="display: inline-flex; align-items: center; padding: 12px 28px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.3s; box-shadow: 0 4px 15px rgba(102,126,234,0.3);" onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 6px 20px rgba(102,126,234,0.4)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 4px 15px rgba(102,126,234,0.3)';">
        <span style="font-size: 1.2rem; margin-right: 0.5rem;">📖</span> View All Blog Posts
    </a>
</div
- **[{{ post.title }}]({{ post.url }})** - <time>{{ post.date | date: "%B %d, %Y" }}</time>
{% endfor %}

<a href="{{ '/blogs' | relative_url }}" class="btn-crosslink" style="display: inline-flex; margin-top: 1rem;"><span style="font-size: 1.2rem; margin-right: 0.5rem;">📖</span> Read More Posts</a>


## 📚 Learning Journey

Explore topic-wise paths and quick intros below.

<div class="projects-list">
    <div class="project-card">
        <h3><a href="{{ '/learning/programming-language/' | relative_url }}">Explore Programming Languages</a></h3>
        <p>All about C, C++, Java, Python and other language basics.</p>
    </div>
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
        <h3><a href="{{ '/learning/4g-5g/' | relative_url }}">4G/5G Networks</a></h3>
        <p>Mobile architecture, LTE, 5G NR, and cellular protocols.</p>
    </div>
    <div class="project-card">
        <h3><a href="{{ '/learning/competitive-programming/' | relative_url }}">Competitive Programming</a></h3>
        <p>Contest strategy, patterns and practice resources.</p>
    </div>
    <dFeatured Projects

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
    {% for project in site.projects limit: 3 %}
    <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 10px rgba(0,0,0,0.08); border-top: 4px solid #764ba2; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 10px rgba(0,0,0,0.08)';">
        <h3 style="margin: 0 0 1rem 0; font-size: 1.3rem;"><a href="{{ project.url }}" style="text-decoration: none; color: #2d3748;">{{ project.title }}</a></h3>
        {% if project.description %}
            <p style="margin: 0 0 1.2rem 0; color: #64748b; line-height: 1.6;">{{ project.description }}</p>
        {% endif %}
        <a href="{{ project.url }}" style="display: inline-flex; align-items: center; color: #667eea; font-weight: 600; text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='#764ba2'; this.style.transform='translateX(5px)';" onmouseout="this.style.color='#667eea'; this.style.transform='translateX(0)';">
            Learn more →
        </a>
    </div>
    {% endfor %}
</div>

<div style="text-align: center;">
    <a href="{{ '/projects' | relative_url }}" style="display: inline-flex; align-items: center; padding: 12px 28px; background: linear-gradient(135deg, #764ba2, #667eea); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.3s; box-shadow: 0 4px 15px rgba(118,75,162,0.3);" onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 6px 20px rgba(118,75,162,0.4)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 4px 15px rgba(118,75,162,0.3)';">
        <span style="font-size: 1.2rem; margin-right: 0.5rem;">🚀</span> View All Projects
    </a>
</div
    {% for project in site.projects limit: 3 %}
    <div class="project-card">
        <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
        {% if project.description %}
            <p>{{ project.description }}</p>
        {% endif %}
    </div>
    {% endfor %}
</div>


<a href="{{ '/projects' | relative_url }}" class="btn-crosslink" style="display: inline-flex; margin-top: 1rem;"><span style="font-size: 1.2rem; margin-right: 0.5rem;">🚀</span> View All Projects</a>


## 💡 About This Site

A comprehensive portfolio and learning hub documenting my **4+ years** in high-performance systems, data plane development, and backend infrastructure. Here you'll find technical deep dives, real-world projects, and learning resources across DSA, system design, networking, and more.

<a href="{{ '/about' | relative_url }}" class="btn-crosslink" style="display: inline-flex; margin-top: 1.5rem;"><span style="font-size: 1.2rem; margin-right: 0.5rem;">👤</span> Learn More About Me</a>

