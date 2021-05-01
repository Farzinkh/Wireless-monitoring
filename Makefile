#
# This is a project Makefile. It is assumed the directory this Makefile resides in is a
# project subdirectory.
#

PROJECT_NAME := app-template

EXTRA_COMPONENT_DIRS := $(IDF_LIB_PATH) #add for esp lib 

include $(IDF_PATH)/make/project.mk

