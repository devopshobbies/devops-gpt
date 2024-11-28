import { useFormContext } from 'react-hook-form';

export interface Checkboxprops {
  fieldName: string;
  label: string;
}

const CheckBox = ({ fieldName, label }: Checkboxprops) => {
  const { register } = useFormContext();
  return (
    <div className="flex gap-2 justify-center items-center">
      <label htmlFor={label}>{label}</label>
      <input
        id={label}
        className=" w-4 h-4 accent-mainOrange-500"
        {...register(fieldName)}
        type="checkbox"
      />
    </div>
  );
};

export default CheckBox;
