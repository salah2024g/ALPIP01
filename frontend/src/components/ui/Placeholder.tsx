interface PlaceholderProps {
  text: string;
}

export function Placeholder({
  text
}: PlaceholderProps) {
  return (
    <div>
      {text}
    </div>
  );
}
