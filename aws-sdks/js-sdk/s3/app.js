import { S3Client } from "@aws-sdk/client-s3";
// Import required AWS SDK clients and commands for Node.js.
import { PutObjectCommand, CreateBucketCommand } from "@aws-sdk/client-s3";



// Set the AWS Region.
const REGION = "us-east-1"; // This is just an example

// Create an Amazon S3 service client object.
const s3Client = new S3Client({ region: REGION });


// Set the parameters
const params = {
  Bucket: "demo-bucket-20349876502983745", // The name of the bucket. For example, 'sample-bucket-101'.
  Key: "file1.txt", // The name of the object. For example, 'sample_upload.txt'.
  Body: "Hello file to upload!", // The content of the object. For example, 'Hello world!".
};

const run = async () => {
  // Create an Amazon S3 bucket.
  try {
    const data = await s3Client.send(
        new CreateBucketCommand({ Bucket: params.Bucket })
    );
    console.log(data);
    console.log("Successfully created a bucket called ", data.Location);
  } catch (err) {
    console.log("Error", err);
  }
  // Create an object and upload it to the Amazon S3 bucket.
  try {
    const results = await s3Client.send(new PutObjectCommand(params));
    console.log(
        "Successfully created " +
        params.Key +
        " and uploaded it to " +
        params.Bucket +
        "/" +
        params.Key
    );
  } catch (err) {
    console.log("Error", err);
  }
};
run();