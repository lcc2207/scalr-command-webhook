$type = Get-Random -InputObject "DEV", "PROD", "QA"
$num  = Get-Random 5
$hostname = ConvertTo-Json @{hostname="$type$num"}
Write-Output $hostname
