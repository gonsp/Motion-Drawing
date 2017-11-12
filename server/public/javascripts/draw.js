var socket = io();
var lastTimestamp;

socket.on('leap-event-client', function (data) {
    var screenY = data.y * window.innerHeight;
    var screenX = data.x * window.innerWidth;
    $("#pointerImg").css({'top': screenY + 'px', 'left': screenX + 'px'});
});

socket.on('trackpad-event-client', function (data) {
    var dataContext = parseInt(curActiveRow) + 1;
    var curentRow = $("div[data-anchor="+dataContext+"]");
    var maybe = curentRow.find(".active");
    var next = maybe.find("canvas");
    var ctx = next[0].getContext("2d");

    if(Date.now() - lastTimestamp > 60) {
        ctx.closePath();
        ctx.beginPath();
    }

    lastTimestamp = Date.now();
    var screenY = data.y * window.innerHeight;
    var screenX = data.x * window.innerWidth;
    ctx.lineTo(screenX, screenY);
    ctx.stroke();
});

$(document).ready(function () {
    window.requestAnimFrame = function () {
        return window.requestAnimationFrame ||
            window.webkitRequestAnimationFrame ||
            window.mozRequestAnimationFrame ||
            window.oRequestAnimationFrame ||
            window.msRequestAnimationFrame ||
            function (callback) {
                callback()
            }
    }();

    $('#fullpage').fullpage({
        //Navigation
        menu: '#menu',
        lockAnchors: false,
        anchors: ['1', '2', '3', '4'],
        navigation: false,
        navigationPosition: 'right',
        navigationTooltips: ['1', '2', '3', '4'],
        showActiveTooltip: false,
        slidesNavigation: false,
        slidesNavPosition: 'bottom',

        //Scrolling
        css3: true,
        scrollingSpeed: 1200,
        autoScrolling: true,
        fitToSection: true,
        fitToSectionDelay: 1000,
        scrollBar: false,
        easing: 'easeInOutCubic',
        easingcss3: 'ease',
        loopBottom: false,
        loopTop: false,
        loopHorizontal: false,
        continuousVertical: false,
        continuousHorizontal: false,
        scrollHorizontally: false,
        interlockedSlides: false,
        dragAndMove: false,
        offsetSections: false,
        resetSliders: false,
        fadingEffect: false,
        normalScrollElements: null,
        scrollOverflow: false,
        scrollOverflowReset: false,
        scrollOverflowOptions: null,
        touchSensitivity: 15,
        normalScrollElementTouchThreshold: 5,
        bigSectionsDestination: null,

        //Accessibility
        keyboardScrolling: false,
        animateAnchor: false,
        recordHistory: true,

        //Design
        controlArrows: false,
        verticalCentered: true,
        sectionsColor: ['#ccc', '#fff'],
        paddingTop: '3em',
        paddingBottom: '10px',
        fixedElements: null,
        responsiveWidth: 0,
        responsiveHeight: 0,
        responsiveSlides: false,
        parallax: false,
        parallaxOptions: {type: 'reveal', percentage: 62, property: 'translate'},

        //Custom selectors
        sectionSelector: '.section',
        slideSelector: '.slide',

        lazyLoading: true,

        //events
        onLeave: function (index, nextIndex, direction) {
            var prevSlide = $('body').attr('class').split('-')[3];
            if (prevSlide != '0') {
                var leavingSection = $(this);
                requestAnimFrame(function () {
                    $.fn.fullpage.moveTo(nextIndex, parseInt(prevSlide));
                    canScroll = false
                    return false;
                });
            }
        },
        afterLoad: function (anchorLink, index) {
            canScroll = true;
        },
        afterRender: function () {
        },
        afterResize: function () {
        },
        afterResponsive: function (isResponsive) {
        },
        afterSlideLoad: function (anchorLink, index, slideAnchor, slideIndex) {
            canScroll = true;
        },
        onSlideLeave: function (anchorLink, index, slideIndex, direction, nextSlideIndex) {
            canScroll = false;
        }
    });
});

var canvasContexts = [];

// Drawing part

function update(jscolor) {
    // 'jscolor' instance can be used as a string
    for (var i = 0; i < canvasContexts.length; i++) {
        canvasContexts[i].strokeStyle = '#' + jscolor
    }
}

$('.c').each(function () {
    var ctx = this.getContext('2d');
    canvasContexts.push(ctx);

    var classes = $(this).attr('class').split(' ');

    this.width = window.innerWidth;
    this.height = window.innerHeight;

    ctx.beginPath();
    ctx.lineWidth = 10;
    ctx.lineJoin = ctx.lineCap = 'round';

    if (classes.includes('can-lt-corner')) {
        $(this).css("margin-left", "40px");
        $(this).css("margin-top", "40px");
    } else if (classes.includes('can-rt-corner')) {
        this.width -= 70;
        $(this).css("margin-top", "40px");
    } else if (classes.includes('can-l')) {
        $(this).css("margin-left", "40px");
    } else if (classes.includes('can-r')) {
        this.width -= 70;
    } else if (classes.includes('can-t')) {
        $(this).css("margin-top", "40px");
    } else if (classes.includes('can-lb-corner')) {
        $(this).css("margin-left", "40px");
        this.height -= 60;
        $(this).css("margin-bottom", "60px");
    } else if (classes.includes('can-rb-corner')) {
        this.width -= 70;
        this.height -= 60;
        $(this).css("margin-bottom", "60px");
    } else if (classes.includes('can-b')) {
        $(this).css("margin-bottom", "60px");
        this.height -= 60;
    }
});
