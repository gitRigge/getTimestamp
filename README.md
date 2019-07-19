# getTimestamp
Get a UNIX timestamp on a Windows OS

## Requirements

The setup script requries [py2exe](http://py2exe.org/) to build the executable.

## Getting Started

Run the following command to get the dist folder which includes the executable.

```
python.exe setup.py py2exe
```

## Usage

Just run the executable in the Windows command line with date and time as paramter.

```
getTimestamp.exe "18.07.2019 12:53"
```

The output is then:

```
1563447180
```

## Usage in batch file

The intention was to use the executable in a batch file like this:

```
SET timestamp=getTimestamp.exe
FOR /f "tokens=1-3 delims=." %%a in ('date /t') do (set mydate=%%a.%%b.%%c)
FOR /f "delims=" %%d in ('%timestamp% "%mydate%18:00"') do (set myts=%%d)
```

The variable %myts% holds then the current UNIX timestamp.