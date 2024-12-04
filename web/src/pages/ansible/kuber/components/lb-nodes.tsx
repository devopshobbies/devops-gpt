import { FormInput } from '@/components/form/form-input';
import { Plus, Trash2 } from 'lucide-react';
import { FC } from 'react';
import { useFieldArray, useFormContext } from 'react-hook-form';

const LBNodes: FC = () => {
  const { control } = useFormContext();

  const { fields, append, remove } = useFieldArray({
    control,
    name: 'lb_nodes',
  });

  return (
    <div>
      <div className="flex items-center mb-2">
        <p className="text-lg font-bold">LB Nodes</p>
        <button type="button" onClick={append} className="ml-4 btn btn-xs">
          Add <Plus className="size-3" />
        </button>
      </div>
      <div className="space-y-2">
        {fields.map((_, nodeIdx) => (
          <div className="relative" key={nodeIdx}>
            <FormInput
              id={`lb_nodes.${nodeIdx}`}
              name={`lb_nodes.${nodeIdx}.value`}
              label=""
            />
            {nodeIdx > 0 && (
              <button
                onClick={() => remove(nodeIdx)}
                className="absolute right-3 top-3"
              >
                <Trash2 className="size-4" />
              </button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default LBNodes;
