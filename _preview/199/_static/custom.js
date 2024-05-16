function getClassOfCheckedCheckboxes(checkboxes) {
  var tags = [];
  if (checkboxes && checkboxes.length > 0) {
    for (var i = 0; i < checkboxes.length; i++) {
      var cb = checkboxes[i];
      if (cb.checked) {
        tags.push(cb.getAttribute("rel"));
      }
    }
  }
  return tags;
}

function change() {
  var domainsCbs = document.querySelectorAll(".domains input[type='checkbox']");
  var packagesCbs = document.querySelectorAll(".packages input[type='checkbox']");

  var domainTags = getClassOfCheckedCheckboxes(domainsCbs);
  var packageTags = getClassOfCheckedCheckboxes(packagesCbs);

  var filters = {
    domains: domainTags,
    packages: packageTags
  };

  filterResults(filters);
}

function filterResults(filters) {
  var rElems = document.querySelectorAll(".tagged-card");
  var hiddenElems = [];

  if (!rElems || rElems.length <= 0) {
    return;
  }

  for (var i = 0; i < rElems.length; i++) {
    var el = rElems[i];
    var isHidden = false; // Initially assume visible

    // Check if any domain or package filter applies
    var hasDomainFilter = filters.domains.length > 0;
    var hasPackageFilter = filters.packages.length > 0;

    if (hasDomainFilter || hasPackageFilter) {
      var isMatching = false; // Check if card matches any filter

      for (var j = 0; j < el.classList.length; j++) {
        var cardClass = el.classList[j];

        // Check if card class matches any domain or package filter
        if (filters.domains.indexOf(cardClass) !== -1 || filters.packages.indexOf(cardClass) !== -1) {
          isMatching = true;
          break; // Stop checking if a matching filter is found
        }
      }

      isHidden = !isMatching; // Hide if no matching filter is found
    }

    if (isHidden) {
      hiddenElems.push(el);
      el.classList.replace("d-flex", "d-none"); // Hide the element
    } else {
      el.classList.replace("d-none", "d-flex"); // Show the element
    }
  }
}
