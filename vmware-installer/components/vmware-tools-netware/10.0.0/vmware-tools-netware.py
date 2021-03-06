#
# Copyright 2009 VMware, Inc.  All rights reserved. -- VMware Confidential
#

"""
VMware Tools ISO Component.

This is the VMIS template component file for the netware Tools ISO, where
netware will be replaced by the name of the specific iso (ie: linux,
windows, freebsd...)
"""
DEST = LIBDIR/'vmware/isoimages'

class ToolsISOnetware(Installer):
   def InitializeInstall(self, old, new, upgrade):
      self.AddTarget('File', 'netware.iso', DEST/'netware.iso')
      self.AddTarget('File', 'netware.iso.sig', DEST/'netware.iso.sig')
