%define device ghost
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto X

%define installable_zip 1

%define straggler_files \
/init.mmi.boot.sh\
/init.mmi.touch.sh\
%{nil}

%include rpm/dhd/droid-hal-device.inc
