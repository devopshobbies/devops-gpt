import { useFormContext } from 'react-hook-form';
import { validateForm } from '../../utils/formValidator';
import { CSSProperties } from 'react';

interface Props {
  fieldName: string;
  label?: string;
  placeholder?: string;
  disabled?: boolean;
  style?: CSSProperties;
}

const TextArea = ({
  fieldName,
  label,
  placeholder,
  style,
  disabled = false,
}: Props) => {
  const {
    register,
    formState: { errors },
  } = useFormContext();

  const error = errors[fieldName];
  return (
    <div className="w-full">
      <div className="label">
        <span className="label-text">{label}</span>
      </div>
      <textarea
        autoFocus
        className={
          'overflow-y-auto w-full border border-slate-300 outline-none focus-within:bg-slate-50 text-stone-600 rounded-md flex h-auto p-4'
        }
        {...register(fieldName, validateForm(fieldName))}
        placeholder={placeholder}
        style={style}
        disabled={disabled}
      />
      <p className="text-red-600 text-sm h-4">{error?.message as string}</p>
    </div>
  );
};

export default TextArea;
