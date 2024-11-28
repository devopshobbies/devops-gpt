import { Button } from '@chakra-ui/react';
import { FormProvider } from 'react-hook-form';
import { IoSendOutline } from 'react-icons/io5';
import ChatBox from '../../components/internal-ui/ChatBox';
import Input from '../../components/internal-ui/Input';
import useFormHandler from '../../hooks/useFormHandler';
import { bugFixMapper } from '../../utils/mapperFunctions';
import useGptStore from '../../utils/store';
import { bugFixDefaultValues, BugFixFields, Endpoints } from '../constants';
import { ApiRequestBugFix, BugFixFormData } from '../models';
import TextArea from '../../components/internal-ui/TextArea';

const BugFix = () => {
  const { request, handleSubmit, onSubmit, formMethods } = useFormHandler<
    BugFixFormData,
    ApiRequestBugFix
  >(bugFixDefaultValues);

  const messages = useGptStore((s) => s.messages);

  const handleFormSubmit = handleSubmit((data) => {
    onSubmit(bugFixMapper(data), data.bugDescription);
  });

  return (
    <FormProvider {...formMethods}>
      <form className="h-full flex flex-col pt-4" onSubmit={handleFormSubmit}>
        <div className="flex flex-wrap gap-2">
          <Input fieldName={BugFixFields.MIN_TOKEN} label="Min token" />
          <Input fieldName={BugFixFields.MAX_TOKEN} label="Max token" />
          <Input fieldName={BugFixFields.SERVICE} label="Service" />
          <Input fieldName={BugFixFields.VERSION} label="Version" />
        </div>

        <div className="flex-1 pb-10 pt-4">
          <ChatBox
            endpoint={Endpoints.POST_FIX}
            request={request}
            messageData={messages}
            id={request?.requestId ?? ''}
          />
        </div>

        <div className="flex sticky gap-2 items-center bottom-0 pb-4 bg-white">
          <TextArea
            placeholder="Write Prompt..."
            style={{ resize: 'none' }}
            fieldName={BugFixFields.BUG_DESCRIPTION}
          />
          <Button
            type="submit"
            bg="orange.600"
            className="hover:bg-orange-500"
            disabled={
              formMethods.getFieldState(BugFixFields.BUG_DESCRIPTION).invalid
            }
          >
            <IoSendOutline className="text-white" />
          </Button>
        </div>
      </form>
    </FormProvider>
  );
};

export default BugFix;
