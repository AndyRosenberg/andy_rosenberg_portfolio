var pics;
var idx;

var interval;
var timer = function(){
  if (interval) { clearInterval(interval) }
  interval = setInterval(function(){
    $('#next').trigger('click');
  }, 6000);
};

function addActive(head) {
  $(head).addClass('header-active');
}

function defineActive() {
  $('.header-active').removeClass('header-active');
  var aftslash = location.href.indexOf('/', 8);
  switch (location.href.slice(aftslash + 1, aftslash + 5)) {
    case 'abou':
      addActive('#about');
      break;
    case 'apps':
      addActive('#apps');
      break;
    case 'blog':
      addActive('#blog');
      break;
    case 'cont':
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
    timer();
  });

  $('#next').click(function(e) {
    e.stopPropagation();
    if (idx + 1 === pics.length) {
      beginning();
    } else {
      next();
    }
    timer();
  });

  timer();

});