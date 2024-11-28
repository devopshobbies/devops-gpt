import { FormProvider } from 'react-hook-form';
import Input from '../../components/internal-ui/Input';
import { basicGenDefaultValues, BasicGenFields, Endpoints } from '../constants';
import { Button } from '@chakra-ui/react';
import TextArea from '../../components/internal-ui/TextArea';

import useGptStore from '../../utils/store';
import ChatBox from '../../components/internal-ui/ChatBox';

import { ApiRequestBasicGen, BasicGenFormData } from '../models';

import { IoSendOutline } from 'react-icons/io5';

import useFormHandler from '../../hooks/useFormHandler';
import { basicGenMapper } from '../../utils/mapperFunctions';

const BasicGen = () => {
  const { formMethods, handleSubmit, onSubmit, request } = useFormHandler<
    BasicGenFormData,
    ApiRequestBasicGen
  >(basicGenDefaultValues);

  const handleFormSubmit = handleSubmit((data) => {
    onSubmit(basicGenMapper(data), data.input);
  });

  const messages = useGptStore((s) => s.messages);

  return (
    <FormProvider {...formMethods}>
      <form className="h-full flex flex-col pt-4" onSubmit={handleFormSubmit}>
        <div className="flex flex-wrap gap-2">
          <Input fieldName={BasicGenFields.MIN_TOKEN} label="Min token" />
          <Input fieldName={BasicGenFields.MAX_TOKEN} label="Max token" />
          <Input fieldName={BasicGenFields.SERVICE} label="Service" />
        </div>
        <div className="flex-1 pb-10 pt-4">
          <ChatBox
            endpoint={Endpoints.POST_BASIC}
            request={request}
            messageData={messages}
            id={request?.requestId ?? ''}
          />
        </div>
        <div className="flex sticky gap-2 items-center bottom-0 pb-4 bg-white">
          <TextArea
            placeholder="Write Prompt..."
            style={{ resize: 'none' }}
            fieldName={BasicGenFields.INPUT}
          />
          <Button
            type="submit"
            bg="orange.600"
            className="hover:bg-orange-500"
            disabled={formMethods.getFieldState(BasicGenFields.INPUT).invalid}
          >
            <IoSendOutline className="text-white" />
          </Button>
        </div>
      </form>
    </FormProvider>
  );
};

export default BasicGen;
