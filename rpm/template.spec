Name:           ros-indigo-epos-hardware
Version:        0.0.3
Release:        0%{?dist}
Summary:        ROS epos_hardware package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-epos-library
Requires:       ros-indigo-hardware-interface
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-transmission-interface
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-epos-library
BuildRequires:  ros-indigo-hardware-interface
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-transmission-interface

%description
A wrapper around the EPOS Command Library to provide easy integration with ROS
control

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Jun 18 2015 Mitchell Wills <mwills@wpi.edu> - 0.0.3-0
- Autogenerated by Bloom

* Fri Mar 06 2015 Mitchell Wills <mwills@wpi.edu> - 0.0.2-0
- Autogenerated by Bloom

* Fri Jan 30 2015 Mitchell Wills <mwills@wpi.edu> - 0.0.1-0
- Autogenerated by Bloom

