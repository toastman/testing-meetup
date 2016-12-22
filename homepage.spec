@objects
    header          css #header .middle-wrapper
    header-icon     css #header-logo
    header-text     css #header h1
    menu            css #menu .middle-wrapper
    content         css #content

= Skeleton =
    @on desktop
        header:
            width 900px
            height ~ 69px
            centered horizontally inside screen 1px

        menu:
            aligned vertically all header
            below header 0 to 1px
            height ~ 164px

    @on mobile
        header-icon:
            width 48px
            height 48px
            inside header 0px left, 5 to 15px top bottom

        menu:
            aligned vertically all header
            below header 0 to 1px
            height ~ 126px

    header-text:
        inside header 5 to 22px top bottom
        near header-icon 15 to 30px right

    content:
        aligned vertically all menu
        below menu 0 to 1px