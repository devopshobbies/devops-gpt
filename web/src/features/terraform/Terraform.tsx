import Docker from "./components/Docker";
import EC2 from "./components/EC2";
import IAM from "./components/IAM";
import S3 from "./components/S3";

const Terraform = () => (
  <div className="py-10 flex flex-col gap-y-5">
    <Docker />
    <EC2 />
    <S3 />
    <IAM />
  </div>
);

export default Terraform;
