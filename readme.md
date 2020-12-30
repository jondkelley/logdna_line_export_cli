# logdna_export_cli

This command will recursively fetch all logs from the logdna export API.

This is useful to get logs beyond the 10,000 line limit as the API does not natively provide pagination.
  
## Install
```
pip3 install logdna_line_export

#or

python setup.py install

# If your system has Python dependency issues, use virtual python environments!
pip3 install virtualenv

virtualenv logdna_line_export_venv
source ./logdna_line_export_venv/bin/activate
pip3 install logdna_line_export
```

## Usage

Example
```
logdna_line_export -k <SERVICE-KEY -q 'app:my_awesome_app' -f 2010-12-01T10:05:45-06:00
```

This will fetch all records from a starting date to now.

## Help

```
Usage: logdna_line_export [OPTIONS]

  This command will recursively fetch all logs from the logdna export API.

  This is useful to get logs beyond the 10,000 line limit as the API does
  not natively provide pagination.

  Authors: jonathan.kelley@logdna.com

Options:
  -q, --query TEXT        The log query you wish to perform  [required]
  -k, --service-key TEXT  Your LogDNA service key found in your settings
                          [required]
  -f, --fromtime TEXT     From date, must be any ISO-8601 compatible date
                          [i.e. 2020-12-01T10:05:45-06:00] or UNIX Epoch in
                          seconds  [required]
  -t, --totime INTEGER    Optional from date, must be any ISO-8601 compatible
                          date [i.e. 2020-12-01T10:05:45-06:00] or UNIX Epoch
                          in seconds
  -h, --host TEXT         Optional change the default LogDNA API host endpoint
                          [default: api.logdna.com]
  -p, --print-date        Print the date conversions, useful for
                          troubleshooting iso8601 conversion
  --help                  Show this message and exit.
```
