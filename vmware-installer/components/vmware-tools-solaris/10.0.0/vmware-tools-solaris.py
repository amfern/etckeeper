#
# Copyright 2009 VMware, Inc.  All rights reserved. -- VMware Confidential
#

"""
VMware Tools ISO Component.

This is the VMIS template component file for the solaris Tools ISO, where
solaris will be replaced by the name of the specific iso (ie: linux,
windows, freebsd...)
"""
DEST = LIBDIR/'vmware/isoimages'

class ToolsISOsolaris(Installer):
   def InitializeInstall(self, old, new, upgrade):
      self.AddTarget('File', 'solaris.iso', DEST/'solaris.iso')
      self.AddTarget('File', 'solaris.iso.sig', DEST/'solaris.iso.sig')
