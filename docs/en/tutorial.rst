
************************
Using the ISO8601 parser
************************

OK, why not date or datetime?
=============================

The notion of a point in time without further context does not
make sense in calendrical calculations. If you dig deep enough,
you will even encounter that February 30th is a valid date. [#]_

.. [#] 1712 in Sweden ;-) http://en.wikipedia.org/wiki/February_30

If you need to store time zone information, there is no easy
way in Python 2.x to store this in a datetime type. In addition,
there is no support for time formats like `24:00`, which is
perfectly valid according to ISO8601.

A package that needs to calculate holidays also needs information
on the country or even the federal state for which the holiday
is valid.

So, no, I do not use the date or datetime type in this package
because the capabilities do not fit my requirements.


Parsing date and time strings
=============================

Introduction
------------

As stated above, the date and datetime types are not used in
this package. So how do you work with the parser then? Well,
I do not know which information you need from a time string,
what you do with it (maybe only displaying the month in a
label) or if you just want to validate a date string.
Therefore, the ISO8601 parser does just that, parsing an
ISO8601 date/time string and returning a dictionary with all
information back to you, including some convenience information
like milliseconds since midnight for the day, if there is a time
part.


Automatic detection of ISO format
---------------------------------

One of the advantages of using this package is that you do not
have to specify the format of the date/time string, the parser
will automatically detect the format used. ISO8601 specifies
the list of valid date and time formats, so there is no need
to provide redundant information.

The input will either comply with ISO8601 rules and return a
dictionary with the results or, in case of the input not being
a valid date/time string, will throw an exception.

To retrieve the date format used (see isoformats_), use the `dateformat` or `timeformat` keys of
the resulting dictionary::

 try:
     result = IsoDate.from_iso_string(my_date_string)
     fmt_used = result['dateformat']
 except Excepion as e:
     print('Oops, not a valid format.')
     print(e)

The list of supported ISO8601 date formats is at isoformats_.


Instantiating IsoDate from a string
-----------------------------------

Use the class method `from_iso_string` to parse a date or a timestamp.
::

 parse = IsoDate.from_iso_string('2005-08-20T05:40:00+0200')

There are optional keyword args to specify `country`, `state` and `separator`.
Country defaults to `'DE'` (after all, I live in Germany <g>) and the state
value defaults to `None` (providing Bavaria as the default would have been
a little bit over the top, wouldn't it?).
The default for the separator character is the capital letter `'T'` as set forth
in the ISO8601 (also allows for a lowercase letter). If you absolutely need to,
change this to a space character.


Parse-only class method
-----------------------

There is a class method `parse_iso_string` that does not return an instance of IsoDate,
but returns the parser result dictionary instead::

    @classmethod
    def parse_iso_string(cls, iso_string, separator='T'):

The reason for this class method is convenience for anyone needing to parse an ISO8601
string that also contains time information. As *dt8601* is designed for day-based
calculations, this method provides an easy method to use the parser alone.

Accessing the ISO8601 parser results
------------------------------------

To access the parsing results, use one of the keys below for
the dictionary returned from the method call. You have to check for
existence of a key before accessing it, because depending on the input string
there might be no time part present. If the key is not self-explanatory, I added
a short description

 * year
 * month
 * day
 * weekday  --  1..7 (monday..sunday)
 * dayofyear  --  1..365 (366 for a leap year)
 * iso_date  --  in YYYY-MM-DD format
 * dateformat  --  the date format used, see isoformats_
 * hour
 * minute
 * second
 * micros  --  microseconds since midnight
 * fraction  --  part of time that contained a fraction value ('hour' | 'minute' | 'second')
 * fraction_value  --  float value with fractional part
 * iso_time  --  time in HH:MM:SS format
 * timeformat  --  the time format used, see isoformats_
 * tz_offset  --  time zone offset in seconds, prefixed by `+` or `-`
 * timezoneformat  --  one of 'Z' | 'HH' | 'HHMM'

Usage would be like so::

 try:
     result = IsoDate.parse_iso_string('2005-08-20T05:40:00+02:00', separator='T'):
     msg = "Microseconds since midnight: {micros} on day {doy} of year {year}"
     print msg.format(micros=result['micros'], doy=result['dayofyear'], year=result['year'])
 except:
     print("Not a valid ISO timestamp")

If you just want to check if a string does contain a valid date/time, check for an exception::

  def is_valid_iso8601(the_string):
      try:
          dt = IsoDate.from_iso_string(the_string)
          result = True
      except Exception:
          result = False
      return result


Format ISO8601 strings
======================

Formatting IsoDate instances
----------------------------

To format a date/time, use the method `to_iso_string` of the `IsoDate` instance and specify the desired output format::

 output =  iso_string('YYYY-WW-D')

Using an invalid output format will raise an exception. The method provides a keyword arg `separator`
that defaults to `'-'`. For the compact format, use an empty string as the separator.


Using the class method
----------------------

If you already have the data and just want to format an ISO string,
use the class method of the IsoDate  class. This method expects
year, month and day values as well as the ISO format string::

  def date_string(cls, year, month, day, isoformat='YYYY-MM-DD', separator='-'):


Additional information
======================

Leap seconds
------------

The package features a list of years with leap seconds as well
as the ability to download the current list of leap seconds by
FTP from a NIST time server.

Using the value `60` for seconds is only allowed at the time of
occurrence for a leap seconds. All other dates will raise a `ValueError`.


.. _isoformats:
ISO formats
-----------

For each format listed below, there is a compact form
without the separator, e.g. YYYYMMDD for YYYY-MM-DD.
For both inputs, the format code returned will be the
long form YYYY-MM-DD.

 * YYYY-MM-DD  --  year, month, day
 * YYYY-MM  --  year, month (default to first day of month)
 * YYYY  --  year (defaults to January, 1st of year)
 * YYYY-WWW  -- year and week number (defaults to the monday starting the week)
 * YYYY-WWW-D  --  year, week number, weekday (1..7)
 * YYYY-DDD  --  year and day of year

Possible time formats are:

 * HH.nnnnnn
 * HHMM.nnnnnn
 * HHMMSS.nnnnnn