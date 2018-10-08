var pics;
var idx;

function addActive(head) {
  $(head).addClass('header-active');
}

function defineActive() {
  $('.header-active').removeClass('header-active');
  switch (location.href.slice(location.href.indexOf('/', 8) + 1)) {
    case 'about':
      addActive('#about');
      break;
    case 'apps':
      addActive('#apps');
      break;
    case 'blog/':
      addActive('#blog');
      break;
    case 'contact':
      addActive('#contact');
      break;
    default:
      addActive('#home');
  }
}

function replacer(n) {
  $('#current-image').fadeOut('slow', function() {
    $('#pic-name').text(pics[n]['name']);
    $('#pic-description').text(pics[n]['description']);
    $('#pic-image').prop('src', pics[n]['image']);
    $('#pic-link').prop('href', pics[n]['link']);
    $('#pic-site').prop('href', pics[n]['site']);
    $('#current-image').fadeIn('slow');
  });
}

function replaceAll(i) {
  $('#pics').data('idx', i);
  replacer(i);
}

function previous() {
  idx -= 1;
  replaceAll(idx);
}

function next() {
  idx += 1;
  replaceAll(idx);
}

function beginning() {
  idx = 0;
  replaceAll(idx);
}

function nd() {
  idx = pics.length - 1;
  replaceAll(idx);
}

$(function() {
  defineActive();

  if ($('#pics').length) {
    pics = $('#pics').data('pics');
    idx = $('#pics').data('idx');
  }

  $('#previous').click(function(e) {
    e.stopPropagation();
    if (idx - 1 < 0) {
      nd();
    } else {
      previous();
    }
  });

  $('#next').click(function(e) {
    e.stopPropagation();
    if (idx + 1 === pics.length) {
      beginning();
    } else {
      next();
    }
  });

  setInterval(function() {
    $('#next').trigger('click');
  }, 6000);

});