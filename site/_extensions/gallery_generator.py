import itertools
import pathlib
import urllib.request
from textwrap import dedent

import yaml
from truncatehtml import truncate


def _grab_binder_link(repo):
    config_url = f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/_config.yml"
    config = urllib.request.urlopen(config_url)
    config_dict = yaml.safe_load(config)
    root = config_dict["sphinx"]["config"]["html_theme_options"]["launch_buttons"]["binderhub_url"]
    end = f"/v2/gh/ProjectPythia/{repo}.git/main"
    url = root + end
    return root, url

def _generate_status_badge_html(repo, github_url):
    binder_root, binder_link = _grab_binder_link(repo)
    return f"""
    <a class="reference external" href="{github_url}/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="{github_url}/actions/workflows/nightly-build.yaml/badge.svg" /></a>
    <a class="reference external" href="{binder_link}"><img alt="Binder" src="{binder_root}/badge_logo.svg" /></a>
    """

def generate_repo_dicts(all_items):

    repo_dicts = []
    for item in all_items:
        repo = item.strip()
        github_url = f"https://github.com/ProjectPythia/{repo}"
        cookbook_url = f"https://projectpythia.org/{repo}/README.html"

        config_url = f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/_config.yml"
        config = urllib.request.urlopen(config_url)
        config_dict = yaml.safe_load(config)

        cookbook_title = config_dict["title"]
        authors = config_dict["author"]
        thumbnail = config_dict["thumbnail"]
        description = config_dict["description"]
        tag_dict = {k: v for k, v in config_dict["tags"].items() if v[0] != None}

        repo_dict = {
            "repo": repo,
            "github_url": github_url,
            "cookbook_url": cookbook_url,
            "cookbook_title": cookbook_title,
            "authors": authors,
            "thumbnail": thumbnail,
            "description": description,
            "tags": tag_dict,
        }

        repo_dicts.append(repo_dict)

    return repo_dicts


def _generate_sorted_tag_keys(repo_dicts):

    key_set = set(
        itertools.chain(*[repo_dict["tags"].keys() for repo_dict in repo_dicts])
    )
    return sorted(key_set)


def _generate_tag_set(repo_dicts, tag_key=None):

    tag_set = set()
    for repo_dict in repo_dicts:
        for k, e in repo_dict["tags"].items():
            if tag_key and k != tag_key:
                continue
            for t in e:
                tag_set.add(t)

    return tag_set

def _generate_tag_menu(repo_dicts, tag_key):

    tag_set = _generate_tag_set(repo_dicts, tag_key)
    tag_list = sorted(tag_set)

    options = "".join(
        f'<li><label class="dropdown-item checkbox {tag_key}"><input type="checkbox" rel={tag.replace(" ", "-")} onchange="change();">&nbsp;{tag}</label></li>'
        for tag in tag_list
    )

    return f"""
<div class="dropdown">

<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="{tag_key}Dropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
{tag_key.title()}
</button>
<ul class="dropdown-menu" aria-labelledby="{tag_key}Dropdown">
{options}
</ul>
</div>
"""

def generate_menu(repo_dicts, submit_btn_txt=None, submit_btn_link=None):

    key_list = _generate_sorted_tag_keys(repo_dicts)

    menu_html = '<div class="d-sm-flex mt-3 mb-4">\n'
    menu_html += '<div class="d-flex gallery-menu">\n'
    if submit_btn_txt:
        menu_html += f'<div><a role="button" class="btn btn-primary btn-sm mx-1" href={submit_btn_link}>{submit_btn_txt}</a></div>\n'
    menu_html += "</div>\n"
    menu_html += '<div class="ml-auto d-flex">\n'
    menu_html += '<div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>\n'
    for tag_key in key_list:
        menu_html += _generate_tag_menu(repo_dicts, tag_key) + "\n"
    menu_html += "</div>\n"
    menu_html += "</div>\n"
    menu_html += '<script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>\n'
    return menu_html

def build_from_repos(
    repo_dicts,
    filename,
    title="Gallery",
    subtitle=None,
    subtext=None,
    menu_html="",
    max_descr_len=300,
):

    # Build the gallery file
    panels_body = []
    for repo_dict in repo_dicts:
        repo = repo_dict["repo"]
        github_url = repo_dict["github_url"]
        status_badges = _generate_status_badge_html(repo, github_url)

        cookbook_url = repo_dict["cookbook_url"]
        cookbook_title = repo_dict["cookbook_title"]

        authors = repo_dict["authors"]
        authors_str = f"<strong>Author:</strong> {authors}"

        thumbnail = repo_dict["thumbnail"]
        thumbnail_url = f"https://raw.githubusercontent.com/ProjectPythia/{repo}/main/{thumbnail}"

        tag_dict = repo_dict["tags"]
        tag_list = sorted((itertools.chain(*tag_dict.values())))
        tag_list_f = [tag.replace(" ", "-") for tag in tag_list]
        tags = [
            f'<span class="badge bg-primary mybadges">{tag}</span>'
            for tag in tag_list_f
        ]
        tags = "\n".join(tags)
        tag_class_str = " ".join(tag_list_f)

        description = repo_dict["description"]
        ellipsis_str = '<a class="modal-btn"> ... more</a>'
        short_description = truncate(description, max_descr_len, ellipsis=ellipsis_str)

        if ellipsis_str in short_description:
            modal_str = f"""
<div class="modal">
<div class="content">
<img src="{thumbnail_url}" class="modal-img" />
<h3 class="display-3">{cookbook_title}</h3>
{authors_str}
<p class="my-2">{description}</p>
<p class="my-2">{tags}</p>
<p class="mt-3 mb-0"><a href="{cookbook_url}" class="btn btn-outline-primary btn-block">Visit Website</a></p>
</div>
</div>
"""
        else:
            modal_str = ""

        panels_body.append(
            f"""\
---
:column: + tagged-card {tag_class_str}

<div class="d-flex gallery-card">
<img src="{thumbnail_url}" class="gallery-thumbnail" />
<div class="container">
<a href="{cookbook_url}" class="text-decoration-none"><h4 class="display-4 p-0">{cookbook_title}</h4></a>
<p class="card-subtitle">{authors_str}</p>
<br/>
<p class="my-2">{short_description}</p>
</div>
</div>
{modal_str}

+++
<div class="tagsandbadges">
{tags}
<div{status_badges}</div>
</div>

"""
        )

    panels_body = "\n".join(panels_body)

    stitle = f"#### {subtitle}" if subtitle else ""
    stext = subtext if subtext else ""

    panels = f"""
# {title}

{stitle}
{stext}

{menu_html}

````{{panels}}
:column: col-12
:card: +mb-4 w-100
:header: d-none
:body: p-3 m-0
:footer: p-1

{dedent(panels_body)}
````

<div class="modal-backdrop"></div>
<script src="/_static/custom.js"></script>
"""

    pathlib.Path(f"{filename}.md").write_text(panels)
