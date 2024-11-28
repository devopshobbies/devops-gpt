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

const Input = ({
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
    <div>
      <div className="label">
        <span className="label-text">{label}</span>
      </div>

      <input
        disabled={disabled}
        className="border border-slate-300 outline-none focus-within:bg-slate-50 text-stone-600 rounded-md flex h-auto p-4"
        {...register(fieldName, validateForm(fieldName))}
        placeholder={placeholder}
        style={style}
      />

      {error && (
        <p className="text-red-600 text-sm">{error?.message as string}</p>
      )}
    </div>
  );
};

export default Input;
