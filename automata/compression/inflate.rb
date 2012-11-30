#!/usr/bin/env ruby -w
################################################################################
# Inflate
################################################################################
# A utility script for automatically inflating archives by detecting their
# type out of the filename extension.
################################################################################

puts ""
puts "Multi-type archive inflation script"
puts "==================================="
puts ""

archive = ARGV[0]
name = File.basename(archive)
extention = File.extname(archive)
puts "Manipulating file " + name + " of extention " + extention
case extention
when ".zip"
    puts "Attempting to inflate zip file " + archive + "."
when ".rar"
    puts "Attempting to inflate rar file " + archive + "."
when ".gz"
    puts "Attempting to inflate gunzipped file " + archive + "."
    cmd = "gunzip " + archive
    if system(cmd)
        puts "Command " + cmd + " successfully executed!"
    else
        puts "Command " + cmd + " failed to execute!"
    end
when ".7z"
    puts "Attempting to inflate zip file " + archive + "."
when ".tgz"
when ".tar.gz"
    puts "Attempting to inflate gunzipped tarball file " + archive + "."
when ".tar"
    puts "Attempting to inflate  tarball file " + archive + "."
else
    puts "Cannot handle the extention type of archive " + archive + "."
end