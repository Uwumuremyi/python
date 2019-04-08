#string formating

integerValue = 4237

print "integer", integerValue
print "Decimal integer %d" % integerValue
print "Hexadecimal integer %x\n" % integerValue

floatValue = 12345.6789

print "Float", floatValue
print "Default float %f" %floatValue
print "Default exponential %e\n" % floatValue


print "Right justify integer (%8d)" % integerValue
print "Left justify integer (%-8d)" % integerValue

stringValue = "String formatting"
print "Force eight digits in integer %.8d" % integerValue
print "Five digits after decimal in float %.5f" % floatValue
print "Fifteen and five characters  allowed in a string:"
print "(%.15s) (%.5s) (%.100s)" % ( stringValue, stringValue, stringValue)