
# Cookbooks Gallery

<div class="subtext">
<p>Pythia Cookbooks provide example workflows on more advanced and domain-specific problems developed by the Pythia community. Cookbooks build on top of skills you learn in <a href="https://foundations.projectpythia.org/landing-page.html">Pythia Foundations</a>.</p>
<p>Cookbooks are created from Jupyter Notebooks that we strive to binderize so each Cookbook can be <a href="https://foundations.projectpythia.org/preamble/how-to-use.html#interacting-with-jupyter-notebooks-in-the-cloud-via-binder">executed in the cloud with a single click from your browser</a>, but in some instances executing a Cookbook will require <a href="https://foundations.projectpythia.org/preamble/how-to-use.html#interacting-with-jupyter-books-locally">running the notebooks locally</a>.</p>
<p>Interested in contributing a new Cookbook or contributing to an existing Cookbook? Great! Please see the <a href="https://github.com/ProjectPythia/.github/blob/main/.github/CONTRIBUTING.md">Project Pythia Cookbook Contributor's Guide</a>, and consider opening a discussion under the <a href="https://discourse.pangeo.io/c/education/project-pythia/60">Project Pythia category of the Pangeo Discourse</a>.</p>
</div>


<div class="d-sm-flex mt-3 mb-4">
<div class="d-flex gallery-menu">
<div><a role="button" class="btn btn-primary btn-sm mx-1" href=https://github.com/ProjectPythia/cookbook-gallery/issues/new?assignees=ProjectPythia%2Feducation&labels=content%2Ccookbook-gallery-submission&template=update-cookbook-gallery.yaml&title=Update+Gallery+with+new+Cookbook>Submit a new Cookbook</a></div>
</div>
<div class="ml-auto d-flex">
<div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>

:::{dropdown} Domains
<div class="dropdown">
<ul>
<li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=AWS-cloud onchange="change();">&nbsp;AWS cloud</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=HRRR-model onchange="change();">&nbsp;HRRR model</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=radar onchange="change();">&nbsp;radar</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=zarr onchange="change();">&nbsp;zarr</label></li>
</ul>
</div>
:::


:::{dropdown} Packages
<div class="dropdown">
<ul>
<li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=Py-Art onchange="change();">&nbsp;Py-Art</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xarray onchange="change();">&nbsp;xarray</label></li>
</ul>
</div>
:::

</div>
</div>
<script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>


::::{grid} 1
:gutter: 4

:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/HRRR-AWS-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/HRRR-AWS-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">HRRR AWS Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Tyle, Kevin, HRRR-AWS Cookbook contributors</p>
<p class="my-2">A cookbook for working with AWS-served HRRR model output data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">AWS-cloud</span>
<span class="badge bg-primary mybadges">HRRR-model</span>
<span class="badge bg-primary mybadges">xarray</span>
<span class="badge bg-primary mybadges">zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/HRRR-AWS-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/HRRR-AWS-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/HRRR-AWS-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/507993773"><img alt="DOI" src="https://zenodo.org/badge/507993773.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/radar-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/radar-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Radar Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Grover, Maxwell, Sherman, Zachary, Sharma, Milind, Ladino, Alfonso, Camron, Crystal, Radar Cookbook contributors</p>
<p class="my-2">A cookbook meant to work with various weather radar data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Py-Art</span>
<span class="badge bg-primary mybadges">radar</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/radar-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/radar-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/radar-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/479066261"><img alt="DOI" src="https://zenodo.org/badge/479066261.svg" /></a>
</div>
</div>

:::



<div class="modal-backdrop"></div>
<script src="../html/_static/custom.js"></script>
