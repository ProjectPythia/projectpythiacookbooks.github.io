from gallery_generator import build_from_repos, generate_menu, generate_repo_dicts


def main(app):

    with open("cookbook_gallery.txt") as fid:
        all_items = fid.readlines()

    repo_dicts = generate_repo_dicts(all_items)

    title = "Cookbooks Gallery"

    subtext = ""
    with open("cookbook_gallery_subtext.md") as fid:
        for line in fid:
            subtext = subtext + line

    submit_btn_link = "https://projectpythia.org/cookbook-guide.html"
    submit_btn_txt = "How can I create a new Cookbook?"
    menu_html = generate_menu(
        repo_dicts, submit_btn_txt=submit_btn_txt, submit_btn_link=submit_btn_link
    )

    build_from_repos(
        repo_dicts, "index", title=title, subtext=subtext, menu_html=menu_html
    )


def setup(app):
    app.connect("builder-inited", main)
