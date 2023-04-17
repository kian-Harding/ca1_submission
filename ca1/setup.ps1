New-S3Bucket -BucketName celebritybucket -Region eu-west-1 -CannedACLName public-read-write

$exampleSchema = New-DDBTableSchema | Add-DDBKeySchema -KeyName "Name" -KeyDataType "S"
$exampleTable = New-DDBTable "CelebRecognize" -Schema $exampleSchema -ReadCapacity 5 -WriteCapacity 5