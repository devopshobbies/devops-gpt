import { FormInput } from '@/components/form/form-input';
import { Plus, Trash2 } from 'lucide-react';
import { FC } from 'react';
import { useFieldArray, useFormContext } from 'react-hook-form';

const K8SMasterNodes: FC = () => {
  const { control } = useFormContext();

  const { fields, append, remove } = useFieldArray({
    control,
    name: 'k8s_master_nodes',
  });

  return (
    <div>
      <div className="flex items-center mb-2">
        <p className="text-lg font-bold">K8s Master Nodes</p>
        <button type="button" onClick={append} className="ml-4 btn btn-xs">
          Add <Plus className="size-3" />
        </button>
      </div>
      <div className="space-y-2">
        {fields.map((_, nodeIdx) => (
          <div className="relative" key={nodeIdx}>
            <FormInput
              id={`k8s_master_nodes.${nodeIdx}`}
              name={`k8s_master_nodes.${nodeIdx}.value`}
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

export default K8SMasterNodes;
