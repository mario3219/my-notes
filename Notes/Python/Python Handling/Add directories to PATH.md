```
# ==== REPLACE this with your folder ====

$folderToAdd = "C:\Your\Directory\Here"

$envName = "Path"

$currentPath = [Environment]::GetEnvironmentVariable($envName, "User")

if ($currentPath -notlike "*$folderToAdd*") {

    $newPath = "$currentPath;$folderToAdd"

    [Environment]::SetEnvironmentVariable($envName, $newPath, "User")

    Write-Output "Added to PATH: $folderToAdd"
} else {
    Write-Output "Directory is already in PATH."
}

% Check if directory was Added

$env:Path -split ";"
```

Or alternatively:

```
Win + R
-> sysdm.cpl
Advanced > Environment Variables
User Variables ... > Path > Edit
```