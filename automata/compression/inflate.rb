#!/usr/bin/env ruby -w
################################################################################
# Inflate
################################################################################
# A utility script for automatically inflating archives by detecting their
# type out of the filename extension.
################################################################################

puts ""
puts "Inflate 1.0     2012 Vassilis Moustakas"
puts "Multi-type archive inflation script"
puts "==================================="
puts ""

archive = ARGV[0]
name = File.basename(archive)
extention = File.extname(archive)
puts "Manipulating file " + name + " of extention " + extention
success = false;
case extention
when ".zip"
    puts "Attempting to inflate zip file " + archive + "."
    cmd = "unzip " + archive
    success = system(cmd)
when ".rar"
    puts "Attempting to inflate rar file " + archive + "."
    cmd = "rar x " + archive
    success = system(cmd)
when ".gz"
    puts "Attempting to inflate gzipped file " + archive + "."
    cmd = "gunzip " + archive
    success = system(cmd)
when ".7z"
    puts "Attempting to inflate 7-zipped file " + archive + "."
    cmd = "7za x " + archive
    success = system(cmd)
when ".tgz"
#when ".tar.gz"
    puts "Attempting to inflate gzipped tarball file " + archive + "."
    cmd = "tar xzvf " + archive
    success = system(cmd)
else
    puts "Cannot handle the extention type of archive " + archive + "."
end

if success
    puts "Command " + cmd + " successfully executed!"
else
    puts "Command " + cmd + " failed to execute!"
end