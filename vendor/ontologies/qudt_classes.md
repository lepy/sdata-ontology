# qudt Classes (Text Tree)

Source: `vendor/ontologies/qudt.ttl`

```text
Aspect Class (AspectClass)

Comment
└── NIST SP~811 Comment (NIST_SP811_Comment)

Data Encoding (DataEncoding)

Date Time String Encoding Type (DateTimeStringEncodingType)

Quantifiable
├── Quantity
│   └── Physical Constant (PhysicalConstant)
└── Quantity value (QuantityValue)
    └── Constant value (ConstantValue)

QUDT Concept (Concept)
├── Base Dimension Magnitude (BaseDimensionMagnitude)
├── Citation
├── Data Item (DataItem)
├── Discipline
├── Encoding
│   ├── Bit Encoding (BitEncodingType)
│   ├── Boolean encoding type (BooleanEncodingType)
│   ├── Byte Encoding (ByteEncodingType)
│   ├── Char Encoding Type (CharEncodingType)
│   ├── Floating Point Encoding (FloatingPointEncodingType)
│   └── Integer Encoding (IntegerEncodingType)
├── Enumerated Value (EnumeratedValue)
│   ├── Cardinality Type (CardinalityType)
│   ├── Endian Type (EndianType)
│   ├── Ordered type (OrderedType)
│   ├── Quantity type (QuantityType)
│   ├── Rule Type (RuleType)
│   ├── Scale type (ScaleType)
│   └── Transform type (TransformType)
├── Enumeration
├── Figure
├── Maths Function Type (MathsFunctionType)
├── Numeric union (NumericUnion)
├── Organization
├── Prefix
│   ├── Binary Prefix (BinaryPrefix)
│   └── Decimal Prefix (DecimalPrefix)
├── Quantity
│   └── Physical Constant (PhysicalConstant)
├── Quantity Kind (abstract) (AbstractQuantityKind)
│   ├── Quantity Kind (QuantityKind)
│   └── User Quantity Kind (UserQuantityKind)
├── Quantity Kind Dimension Vector (QuantityKindDimensionVector)
│   ├── CGS Dimension vector (QuantityKindDimensionVector_CGS)
│   │   ├── CGS EMU Dimension vector (QuantityKindDimensionVector_CGS-EMU)
│   │   ├── CGS ESU Dimension vector (QuantityKindDimensionVector_CGS-ESU)
│   │   ├── CGS GAUSS Dimension vector (QuantityKindDimensionVector_CGS-GAUSS)
│   │   └── CGS LH Dimension vector (QuantityKindDimensionVector_CGS-LH)
│   ├── Imperial dimension vector (QuantityKindDimensionVector_Imperial)
│   ├── ISO Dimension vector (QuantityKindDimensionVector_ISO)
│   └── Quantity Kind Dimension vector (SI) (QuantityKindDimensionVector_SI)
├── Quantity value (QuantityValue)
│   └── Constant value (ConstantValue)
├── QUDT Datatype (Datatype)
│   └── Scalar Datatype (ScalarDatatype)
├── Rule
├── Scale
│   ├── Enumeration scale (EnumerationScale)
│   ├── Interval scale (IntervalScale)
│   ├── Nominal scale (NominalScale)
│   ├── Ordinal scale (OrdinalScale)
│   └── Ratio scale (RatioScale)
├── Symbol
├── System of Quantity Kinds (SystemOfQuantityKinds)
├── System of Units (SystemOfUnits)
└── Unit
    ├── Contextual Unit (ContextualUnit)
    ├── Derived Unit (DerivedUnit)
    └── Dimensionless Unit (DimensionlessUnit)
        ├── Angle unit (AngleUnit)
        │   ├── Plane Angle Unit (PlaneAngleUnit)
        │   └── Solid Angle Unit (SolidAngleUnit)
        ├── Counting Unit (CountingUnit)
        ├── Currency Unit (CurrencyUnit)
        └── Logarithmic Unit (LogarithmicUnit)
```
