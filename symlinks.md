Here is the symlink file, just in case.

ACTION=="add", SUBSYSTEM=="tty", ATTRS{idVendor}=="06cd", ATTRS{idProduct}=="0121", SYMLINK+="toppress"

ACTION=="add", SUBSYSTEM=="tty", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0043", SYMLINK+="arduino"

ACTION=="add", SUBSYSTEM=="tty", ATTRS{serial}=="DCAWb115819", SYMLINK+="botpress"

ACTION=="add", SUBSYSTEM=="tty", ATTRS{serial}=="EJCZb11A920", SYMLINK+="compress"
