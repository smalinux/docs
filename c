#👉 What libs are REALLY linked against my exec file?
$ ldd execsnoop
    linux-vdso.so.1 (0x00007ffe827e9000)
    libelf.so.1 => /lib/x86_64-linux-gnu/libelf.so.1 (0x00007f86382bb000)
    libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f863829f000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f8638077000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f8638351000)


#👉  Is this symbol REALLY exist in my installed lib?
$ grep -l gelf_getshdr /usr/lib/x86_64-linux-gnu/libelf.*
    /usr/lib/x86_64-linux-gnu/libelf.a
    /usr/lib/x86_64-linux-gnu/libelf.so
    /usr/lib/x86_64-linux-gnu/libelf.so.1


System Programming:
https://stackoverflow.com/q/12591074/5688267

#👉 Super power debugger
. Htop CRT_handleSIGSEGV(int signal)
. printf/dump_stack/backtrace_symbols(3)
. valgrind & addresssanitizer
. cgdb (using ncurses)
. gdb TUI

#👉 C language Profilers
https://stackoverflow.com/q/1794816/5688267

#👉 Unit tesing libraries
.
.

#👉 Awesome c tools - nice to read & study them line by line
https://github.com/3proxy/3proxy
https://github.com/stevenhoneyman/l3afpad
https://github.com/git/git
https://github.com/mcuelenaere/fsv
#https://github.com/pengutronix/genimage
https://github.com/cgdb/cgdb
https://github.com/sysstat/sysstat
https://github.com/WayneD/rsync/


#👉 code navigation
. dump_stack & Htop CRT_handleSIGSEGV for c tags -_-
. ack & rg
. ctags

#👉 macros is evil
# feeh code bases kteer btwld functions bel macros. law el author shreer
# mabyktbsh esm el functions ele btetwld fel comment am law dwrt mesh 7atla2ee
# 3'eer el callsites we mesh 7atla2ee el definition mazkoora fe ay mkan :))
$ rg '##\w+\(' /usr/src/linux


# Use designated initializers whenever possible.
# https://github.com/performancecopilot/pcp/commit/ef9161584a9481599d271734b08c5afc8be41989
metrics[COMM] = (struct pmdaMetric)
- { /* m_user */ NULL,
-  { /* m_desc */
-      PMDA_PMID(cluster_id, 0), PM_TYPE_STRING, indom_id_mapping[EXECSNOOP_INDOM],
-      PM_SEM_INSTANT, PMDA_PMUNITS(0, 0, 0, 0, 0, 0)
+  .m_desc = {
+      .pmid  = PMDA_PMID(cluster_id, 0),
+      .type  = PM_TYPE_STRING,
+      .indom = indom_id_mapping[EXECSNOOP_INDOM],
+      .sem   = PM_SEM_INSTANT,
+      .units = PMDA_PMUNITS(0, 0, 0, 0, 0, 0),
+  }
};
