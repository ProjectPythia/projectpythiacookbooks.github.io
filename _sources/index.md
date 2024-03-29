
# Cookbooks Gallery
=================


Pythia Cookbooks provide example workflows on more advanced and domain-specific problems developed by the Pythia community. Cookbooks build on top of skills you learn in [Pythia Foundations](https://foundations.projectpythia.org/landing-page.html).

Cookbooks are created from Jupyter Notebooks that we strive to binderize so each Cookbook can be [executed in the cloud with a single click from your browser](https://foundations.projectpythia.org/preamble/how-to-use.html#interacting-with-jupyter-notebooks-in-the-cloud-via-binder), but in some instances executing a Cookbook will require [running the notebooks locally](https://foundations.projectpythia.org/preamble/how-to-use.html#interacting-with-jupyter-books-locally).

Interested in contributing a new Cookbook or contributing to an existing Cookbook? Great! Please see the [Project Pythia Cookbook Contributor's Guide](https://github.com/ProjectPythia/.github/blob/main/.github/CONTRIBUTING.md), and consider opening a discussion under the [Project Pythia category of the Pangeo Discourse](https://discourse.pangeo.io/c/education/project-pythia/60).


<div class="d-sm-flex mt-3 mb-4">
<div class="d-flex gallery-menu">
<div><a role="button" class="btn btn-primary btn-sm mx-1" href=https://github.com/ProjectPythia/cookbook-gallery/issues/new?assignees=ProjectPythia%2Feducation&labels=content%2Ccookbook-gallery-submission&template=update-cookbook-gallery.yaml&title=Update+Gallery+with+new+Cookbook>Submit a new Cookbook</a></div>
</div>
<div class="ml-auto d-flex">
<div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>

<div class="dropdown">

<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="domainsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
Domains
</button>
<ul class="dropdown-menu" aria-labelledby="domainsDropdown">
<li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=3D-visualizations onchange="change();">&nbsp;3D visualizations</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=AWS-Cloud onchange="change();">&nbsp;AWS Cloud</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=AWS-cloud onchange="change();">&nbsp;AWS cloud</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Basemaps onchange="change();">&nbsp;Basemaps</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Data-Access onchange="change();">&nbsp;Data Access</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Data-access onchange="change();">&nbsp;Data access</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=GIS onchange="change();">&nbsp;GIS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Geospatial-data onchange="change();">&nbsp;Geospatial data</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=HRRR-model onchange="change();">&nbsp;HRRR model</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=NASA-EarthData-GIBS onchange="change();">&nbsp;NASA EarthData GIBS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Satellite-imagery onchange="change();">&nbsp;Satellite imagery</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=Spatial-analysis onchange="change();">&nbsp;Spatial analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=atmosphere onchange="change();">&nbsp;atmosphere</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=climate onchange="change();">&nbsp;climate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=climate-model onchange="change();">&nbsp;climate model</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-science onchange="change();">&nbsp;data science</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=geospatial onchange="change();">&nbsp;geospatial</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=interactive-visualization onchange="change();">&nbsp;interactive-visualization</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=land-model onchange="change();">&nbsp;land model</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=machine-learning onchange="change();">&nbsp;machine learning</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=meteorology onchange="change();">&nbsp;meteorology</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=ml onchange="change();">&nbsp;ml</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=oceanography onchange="change();">&nbsp;oceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=particles onchange="change();">&nbsp;particles</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=radar onchange="change();">&nbsp;radar</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=satellite onchange="change();">&nbsp;satellite</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=scientific-software-engineering onchange="change();">&nbsp;scientific software engineering</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=sentinel-2 onchange="change();">&nbsp;sentinel-2</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=sustainability onchange="change();">&nbsp;sustainability</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=visualization onchange="change();">&nbsp;visualization</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=weather onchange="change();">&nbsp;weather</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=zarr onchange="change();">&nbsp;zarr</label></li>
</ul>
</div>


<div class="dropdown">

<button class="btn btn-sm btn-outline-primary mx-1 dropdown-toggle" type="button" id="packagesDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
Packages
</button>
<ul class="dropdown-menu" aria-labelledby="packagesDropdown">
<li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=IPython onchange="change();">&nbsp;IPython</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=Py-Art onchange="change();">&nbsp;Py-Art</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=Pyresample onchange="change();">&nbsp;Pyresample</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cartopy onchange="change();">&nbsp;cartopy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=dask onchange="change();">&nbsp;dask</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=datashader onchange="change();">&nbsp;datashader</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=geocat-viz onchange="change();">&nbsp;geocat-viz</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=geoviews onchange="change();">&nbsp;geoviews</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=holoviews onchange="change();">&nbsp;holoviews</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=hvPlot onchange="change();">&nbsp;hvPlot</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=hvplot onchange="change();">&nbsp;hvplot</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake onchange="change();">&nbsp;intake</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-esm onchange="change();">&nbsp;intake-esm</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-markdown onchange="change();">&nbsp;intake-markdown</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-xarray onchange="change();">&nbsp;intake-xarray</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=kerchunk onchange="change();">&nbsp;kerchunk</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=matplotlib onchange="change();">&nbsp;matplotlib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=metpy onchange="change();">&nbsp;metpy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=numpy onchange="change();">&nbsp;numpy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=odc.stac onchange="change();">&nbsp;odc.stac</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=owslib onchange="change();">&nbsp;owslib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=panel onchange="change();">&nbsp;panel</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=planetary-computer onchange="change();">&nbsp;planetary-computer</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=seaborn onchange="change();">&nbsp;seaborn</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=tensorflow onchange="change();">&nbsp;tensorflow</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=verde onchange="change();">&nbsp;verde</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xESMF onchange="change();">&nbsp;xESMF</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xarray onchange="change();">&nbsp;xarray</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xbatcher onchange="change();">&nbsp;xbatcher</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xesmf onchange="change();">&nbsp;xesmf</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=zarr onchange="change();">&nbsp;zarr</label></li>
</ul>
</div>

</div>
</div>
<script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>


::::{grid} 1
:gutter: 4

:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/cesm-lens-aws-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/cesm-lens-aws-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">CESM LENS on AWS Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Banihirwe, Anderson, Bonnlander, Brian, de La Beaujardière, Jeff, Henderson, Scott, CESM LENS on AWS Cookbook contributors</p>
<p class="my-2">Notebooks developed to demonstrate analysis of CESM LENS data publicly available on Amazon S3 (us-west-2 region) using Xarray and Dask. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">climate</span>
<span class="badge bg-primary mybadges">dask</span>
<span class="badge bg-primary mybadges">intake-esm</span>
<span class="badge bg-primary mybadges">xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/cesm-lens-aws-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/cesm-lens-aws-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/cesm-lens-aws-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/509240024"><img alt="DOI" src="https://zenodo.org/badge/509240024.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/cmip6-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/cmip6-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">CMIP6 Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Abernathey, Ryan, Drake, Henri, Ford, Robert R., CMIP6 Cookbook contributors</p>
<p class="my-2">Examples of analysis of Google Cloud CMIP6 data using Pangeo tools. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">climate</span>
<span class="badge bg-primary mybadges">intake-esm</span>
<span class="badge bg-primary mybadges">xesmf</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/cmip6-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/cmip6-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/cmip6-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/507993770"><img alt="DOI" src="https://zenodo.org/badge/507993770.svg" /></a>
</div>
</div>

:::


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


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/intake-cookbook/main/thumbnail.svg" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/intake-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Intake Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Morley, James, Intake Cookbook contributors</p>
<p class="my-2">This cookbook shows examples of using and creating Intake catalogs to access data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Data-access</span>
<span class="badge bg-primary mybadges">intake</span>
<span class="badge bg-primary mybadges">intake-markdown</span>
<span class="badge bg-primary mybadges">intake-xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/intake-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/intake-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/intake-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/512825541"><img alt="DOI" src="https://zenodo.org/badge/512825541.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/landsat-ml-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/landsat-ml-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Landsat ML Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Roumis, Demetris, Landsat ML Cookbook contributors</p>
<p class="my-2">Machine learning on Landsat data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">climate</span>
<span class="badge bg-primary mybadges">dask</span>
<span class="badge bg-primary mybadges">hvPlot</span>
<span class="badge bg-primary mybadges">intake</span>
<span class="badge bg-primary mybadges">ml</span>
<span class="badge bg-primary mybadges">satellite</span>
<span class="badge bg-primary mybadges">xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/landsat-ml-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/landsat-ml-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/landsat-ml-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/563445694"><img alt="DOI" src="https://zenodo.org/badge/563445694.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/kerchunk-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/kerchunk-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Kerchunk Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Hagen, Norland Raphael, Kerchunk Cookbook contributors</p>
<p class="my-2">Kerchunk provides cloud-friendly access to archival data. With Kerchunk you can read collections of legacy file formats (NetCDF, GRIB2 etc.) as if they were ARCO (Analysis-Ready Cloud-Optimized) formats such as Zarr, without creating a copy of the original dataset. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">AWS-Cloud</span>
<span class="badge bg-primary mybadges">Data-Access</span>
<span class="badge bg-primary mybadges">HRRR-model</span>
<span class="badge bg-primary mybadges">intake</span>
<span class="badge bg-primary mybadges">kerchunk</span>
<span class="badge bg-primary mybadges">xarray</span>
<span class="badge bg-primary mybadges">zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/kerchunk-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/kerchunk-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/kerchunk-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/588661659"><img alt="DOI" src="https://zenodo.org/badge/588661659.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/xbatcher-ML-1-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/xbatcher-ML-1-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">xbatcher for Machine Learning Part 1 Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Dupuis, Christopher, Sinha, Anirban, Abernathey, Ryan, xbatcher for Machine Learning Part 1 Cookbook contributors</p>
<p class="my-2">A complete workflow for a convolutional neural network using xbatcher. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">IPython</span>
<span class="badge bg-primary mybadges">data-science</span>
<span class="badge bg-primary mybadges">intake</span>
<span class="badge bg-primary mybadges">machine-learning</span>
<span class="badge bg-primary mybadges">matplotlib</span>
<span class="badge bg-primary mybadges">numpy</span>
<span class="badge bg-primary mybadges">oceanography</span>
<span class="badge bg-primary mybadges">scientific-software-engineering</span>
<span class="badge bg-primary mybadges">tensorflow</span>
<span class="badge bg-primary mybadges">xarray</span>
<span class="badge bg-primary mybadges">xbatcher</span>
<span class="badge bg-primary mybadges">zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/xbatcher-ML-1-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/xbatcher-ML-1-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/xbatcher-ML-1-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/597998597"><img alt="DOI" src="https://zenodo.org/badge/597998597.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/dask-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/dask-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Dask Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Sobhani, Negin, Brian, Vanderwende, Cherian, Deepak, Kirk, Ben, Dask Cookbook contributors</p>
<p class="my-2">A cookbook for Dask workflows. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">dask</span>
<span class="badge bg-primary mybadges">xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/dask-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/dask-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="http://binder.projectpythia.org/v2/gh/ProjectPythia/dask-cookbook.git/main"><img alt="Binder" src="http://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/610934658"><img alt="DOI" src="https://zenodo.org/badge/610934658.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/ERA5_interactive-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/ERA5_interactive-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">ARCO ERA-5 Interactive Visualization Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Tyle, Kevin, Barletta, Michael, ARCO ERA-5 Cookbook contributors</p>
<p class="my-2">A cookbook to interactively explore and visualize ERA-5 data in ARCO format. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">geoviews</span>
<span class="badge bg-primary mybadges">meteorology</span>
<span class="badge bg-primary mybadges">panel</span>
<span class="badge bg-primary mybadges">xarray</span>
<span class="badge bg-primary mybadges">zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/ERA5_interactive-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/ERA5_interactive-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/ERA5_interactive-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/657280462"><img alt="DOI" src="https://zenodo.org/badge/657280462.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/web-map-feature-services-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/web-map-feature-services-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Web Map / Feature Services Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Huang, Andrew, Web Map / Feature Services Cookbook contributors</p>
<p class="my-2">Learn how to use web map and feature services to easily and quickly provide spatial context, without the need to download and process GBs of data! </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Basemaps</span>
<span class="badge bg-primary mybadges">GIS</span>
<span class="badge bg-primary mybadges">Geospatial-data</span>
<span class="badge bg-primary mybadges">NASA-EarthData-GIBS</span>
<span class="badge bg-primary mybadges">Satellite-imagery</span>
<span class="badge bg-primary mybadges">Spatial-analysis</span>
<span class="badge bg-primary mybadges">cartopy</span>
<span class="badge bg-primary mybadges">geoviews</span>
<span class="badge bg-primary mybadges">hvPlot</span>
<span class="badge bg-primary mybadges">owslib</span>
<span class="badge bg-primary mybadges">panel</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/web-map-feature-services-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/web-map-feature-services-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/web-map-feature-services-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/653301659"><img alt="DOI" src="https://zenodo.org/badge/653301659.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/interactive-sentinel-2-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/interactive-sentinel-2-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Sentinel-2 L2A Interactive Dashboard</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Das, Pritam, This Cookbook contributors</p>
<p class="my-2">This Project Pythia Cookbook provides a recipe for building an interactive dashboard for the Sentinel-2 L2A satellite imagery using the holoviews ecosystem. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">dask</span>
<span class="badge bg-primary mybadges">geoviews</span>
<span class="badge bg-primary mybadges">hvplot</span>
<span class="badge bg-primary mybadges">interactive-visualization</span>
<span class="badge bg-primary mybadges">odc.stac</span>
<span class="badge bg-primary mybadges">panel</span>
<span class="badge bg-primary mybadges">planetary-computer</span>
<span class="badge bg-primary mybadges">satellite</span>
<span class="badge bg-primary mybadges">sentinel-2</span>
<span class="badge bg-primary mybadges">xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/interactive-sentinel-2-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/interactive-sentinel-2-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/interactive-sentinel-2-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/656355201"><img alt="DOI" src="https://zenodo.org/badge/656355201.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/gridding-cookbook/main/grid_thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/gridding-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">(re)Gridding with xarray</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Martin, Thomas, (re)Gridding with xarray contributors</p>
<p class="my-2">A small collection of notebooks that explores some (re)gridding options within the Xarray ecosystem. The thumbnail image was created with the assistance of DALL·E 2. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Pyresample</span>
<span class="badge bg-primary mybadges">verde</span>
<span class="badge bg-primary mybadges">xESMF</span>
<span class="badge bg-primary mybadges">xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/gridding-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/gridding-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/gridding-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/540167581"><img alt="DOI" src="https://zenodo.org/badge/540167581.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/gridding-cookbook/main/grid_thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/gridding-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">(re)Gridding with xarray</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Martin, Thomas, (re)Gridding with xarray contributors</p>
<p class="my-2">A small collection of notebooks that explores some (re)gridding options within the Xarray ecosystem. The thumbnail image was created with the assistance of DALL·E 2. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Pyresample</span>
<span class="badge bg-primary mybadges">verde</span>
<span class="badge bg-primary mybadges">xESMF</span>
<span class="badge bg-primary mybadges">xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/gridding-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/gridding-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/gridding-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/540167581"><img alt="DOI" src="https://zenodo.org/badge/540167581.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/advanced-viz-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/advanced-viz-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Advanced Visualization Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Kent, Julia, Zacharias, Anissa, Eroglu, Orhan, Chmielowiec, Philip, Clyne, John, Advanced Visualization Cookbook contributors</p>
<p class="my-2">This Cookbook demonstrates advanced plotting routines using the Python packages matplotlib, cartopy, metpy, and geocat-viz. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">cartopy</span>
<span class="badge bg-primary mybadges">datashader</span>
<span class="badge bg-primary mybadges">geocat-viz</span>
<span class="badge bg-primary mybadges">matplotlib</span>
<span class="badge bg-primary mybadges">metpy</span>
<span class="badge bg-primary mybadges">seaborn</span>
<span class="badge bg-primary mybadges">visualization</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/advanced-viz-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/advanced-viz-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/advanced-viz-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/671205314"><img alt="DOI" src="https://zenodo.org/badge/671205314.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/unstructured-grid-viz-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/unstructured-grid-viz-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Unstructured Grids Visualization Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Eroglu, Orhan, Chmielowiec, Philip, Jain, Rajeev, Franda, Ian, Unstructured Grids Visualization Cookbook contributors</p>
<p class="my-2">This Cookbook is a comprehensive showcase of workflows  </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">cartopy</span>
<span class="badge bg-primary mybadges">datashader</span>
<span class="badge bg-primary mybadges">holoviews</span>
<span class="badge bg-primary mybadges">hvplot</span>
<span class="badge bg-primary mybadges">visualization</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/unstructured-grid-viz-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/669999524"><img alt="DOI" src="https://zenodo.org/badge/669999524.svg" /></a>
</div>
</div>

:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/na-cordex-viz-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/na-cordex-viz-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">NA-CORDEX Visualization Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Bonnlander, Brian, McGinnis, Seth, Banihirwe, Anderson, Nienhouse, Eric, de La Beaujardière, Jeff, NA-CORDEX Visualization Cookbook contributors</p>
<p class="my-2">A notebook for visualizing data from the NA-CORDEX dataset. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">atmosphere</span>
<span class="badge bg-primary mybadges">climate</span>
<span class="badge bg-primary mybadges">climate-model</span>
<span class="badge bg-primary mybadges">dask</span>
<span class="badge bg-primary mybadges">geospatial</span>
<span class="badge bg-primary mybadges">intake-esm</span>
<span class="badge bg-primary mybadges">land-model</span>
<span class="badge bg-primary mybadges">matplotlib</span>
<span class="badge bg-primary mybadges">sustainability</span>
<span class="badge bg-primary mybadges">xarray</span>
<span class="badge bg-primary mybadges">zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/na-cordex-viz-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/na-cordex-viz-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/na-cordex-viz-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/635958518"><img alt="DOI" src="https://zenodo.org/badge/635958518.svg" /></a>
</div>
</div>

:::



<div class="modal-backdrop"></div>
<script src="/_static/custom.js"></script>
