---
layout: archive
title: ""
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

# Journal Articles
{% for post in site.publications reversed %}
  {% if post.pubtype == 'journal' %}
      {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}

# Conference Papers
{% for post in site.publications reversed %}
  {% if post.pubtype == 'conference' %}
      {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}
