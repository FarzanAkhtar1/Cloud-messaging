#############################################################################
# Generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#  Mar 23, 2020 03:15:46 PM GMT  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top50 {base} {
    global vTcl
    if {$base == ""} {
        set base .top50
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 600x450+866+602
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4484 1421
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "LoginPage"
    vTcl:DefineAlias "$top" "LoginPage" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra52 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 385 -width 545 
    vTcl:DefineAlias "$top.fra52" "Frame" vTcl:WidgetProc "LoginPage" 1
    set site_3_0 $top.fra52
    message $site_3_0.mes54 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Login -width 81 
    vTcl:DefineAlias "$site_3_0.mes54" "Message1" vTcl:WidgetProc "LoginPage" 1
    message $site_3_0.mes55 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Password
} -width 81 
    vTcl:DefineAlias "$site_3_0.mes55" "Message2" vTcl:WidgetProc "LoginPage" 1
    entry $site_3_0.ent56 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 234 
    vTcl:DefineAlias "$site_3_0.ent56" "EntryLogin" vTcl:WidgetProc "LoginPage" 1
    entry $site_3_0.ent59 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 234 
    vTcl:DefineAlias "$site_3_0.ent59" "EntryPassword" vTcl:WidgetProc "LoginPage" 1
    message $site_3_0.mes60 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Welcome, please login to the database} -width 309 
    vTcl:DefineAlias "$site_3_0.mes60" "Message3" vTcl:WidgetProc "LoginPage" 1
    button $site_3_0.but62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Login 
    vTcl:DefineAlias "$site_3_0.but62" "BtnLogin" vTcl:WidgetProc "LoginPage" 1
    button $site_3_0.but63 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Back 
    vTcl:DefineAlias "$site_3_0.but63" "BtnBack" vTcl:WidgetProc "LoginPage" 1
    place $site_3_0.mes54 \
        -in $site_3_0 -x 0 -relx 0.202 -y 0 -rely 0.312 -width 0 \
        -relwidth 0.149 -height 0 -relheight 0.208 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes55 \
        -in $site_3_0 -x 0 -relx 0.22 -y 0 -rely 0.597 -width 0 \
        -relwidth 0.149 -height 0 -relheight 0.145 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent56 \
        -in $site_3_0 -x 0 -relx 0.385 -y 0 -rely 0.39 -width 234 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent59 \
        -in $site_3_0 -x 0 -relx 0.385 -y 0 -rely 0.623 -width 234 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes60 \
        -in $site_3_0 -x 0 -relx 0.239 -y 0 -rely 0.13 -width 0 \
        -relwidth 0.567 -height 0 -relheight 0.083 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but62 \
        -in $site_3_0 -x 0 -relx 0.899 -y 0 -rely 0.909 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but63 \
        -in $site_3_0 -x 0 -relx 0.018 -y 0 -rely 0.909 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra52 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.067 -width 0 -relwidth 0.908 \
        -height 0 -relheight 0.856 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top50 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

