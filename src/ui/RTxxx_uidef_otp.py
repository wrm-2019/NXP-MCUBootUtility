import wx
import sys, os

kEfuseFieldColor_Valid  = wx.Colour( 141, 180, 226 )

efusemapIndexDict_RTxxx  = {'kOtpIndex_START' :0x0,

                            'kOtpIndex_BOOT_CFG0' :0x60,
                            'kOtpIndex_BOOT_CFG1' :0x61,
                            'kOtpIndex_BOOT_CFG2' :0x62,
                            'kOtpIndex_BOOT_CFG3' :0x63,

                            'kOtpEntryModeRegion0IndexStart' :0x04,
                            'kOtpEntryModeRegion0IndexEnd'   :0x04,
                            'kOtpEntryModeRegion1IndexStart' :0x08,
                            'kOtpEntryModeRegion1IndexEnd'   :0x09,
                            }

