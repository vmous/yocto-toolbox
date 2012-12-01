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
    cmd = "unzip " + archive
    if system(cmd)
        puts "Command " + cmd + " successfully executed!"
    else
        puts "Command " + cmd + " failed to execute!"
    end
when ".rar"
    puts "Attempting to inflate rar file " + archive + "."
    cmd = "rar x " + archive
    if system(cmd)
        puts "Command " + cmd + " successfully executed!"
    else
        puts "Command " + cmd + " failed to execute!"
    end
when ".gz"
    puts "Attempting to inflate gzipped file " + archive + "."
    cmd = "gunzip " + archive
    if system(cmd)
        puts "Command " + cmd + " successfully executed!"
    else
        puts "Command " + cmd + " failed to execute!"
    end
when ".7z"
    puts "Attempting to inflate 7-zipped file " + archive + "."
    cmd = "7za x " + archive
    if system(cmd)
        puts "Command " + cmd + " successfully executed!"
    else
        puts "Command " + cmd + " failed to execute!"
    end
when ".tgz"
#when ".tar.gz"
    puts "Attempting to inflate gzipped tarball file " + archive + "."
    cmd = "tar xzvf " + archive
    if system(cmd)
        puts "Command " + cmd + " successfully executed!"
    else
        puts "Command " + cmd + " failed to execute!"
    end
else
    puts "Cannot handle the extention type of archive " + archive + "."
end